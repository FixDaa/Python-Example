import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                            QScrollArea, QFrame, QGridLayout)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage, QFont, QIcon
import instaloader
from PIL import Image
import requests
from io import BytesIO

class InstagramWorker(QThread):
    finished = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, username):
        super().__init__()
        self.username = username

    def run(self):
        try:
            L = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(L.context, self.username)
            
            # Profil fotoğrafını indir
            profile_pic_url = profile.profile_pic_url
            response = requests.get(profile_pic_url)
            profile_pic = Image.open(BytesIO(response.content))
            
            # Son 3 gönderiyi al
            recent_posts = []
            for post in profile.get_posts():
                if len(recent_posts) >= 3:
                    break
                
                # Gönderi resmini indir
                if not post.is_video:
                    post_pic_url = post.url
                    response = requests.get(post_pic_url)
                    post_pic = Image.open(BytesIO(response.content))
                    post_pic.save(f"temp_post_{len(recent_posts)}.jpg")
                
                post_data = {
                    'url': post.url,
                    'likes': post.likes,
                    'comments': post.comments,
                    'caption': post.caption if post.caption else "",
                    'date': post.date_local.strftime("%d/%m/%Y"),
                    'is_video': post.is_video,
                    'image_path': f"temp_post_{len(recent_posts)}.jpg" if not post.is_video else None
                }
                recent_posts.append(post_data)
            
            # Profil bilgilerini topla
            profile_data = {
                'username': profile.username,
                'full_name': profile.full_name,
                'biography': profile.biography,
                'followers': profile.followers,
                'following': profile.followees,
                'is_private': profile.is_private,
                'is_verified': profile.is_verified,
                'profile_pic': profile_pic,
                'external_url': profile.external_url,
                'posts_count': profile.mediacount,
                'recent_posts': recent_posts,
                'business_category': profile.business_category_name if hasattr(profile, 'business_category_name') else None,
                'business_email': profile.business_email if hasattr(profile, 'business_email') else None,
                'business_phone': profile.business_phone_number if hasattr(profile, 'business_phone_number') else None
            }
            
            self.finished.emit(profile_data)
        except Exception as e:
            self.error.emit(str(e))

class InstagramViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instagram Profil Görüntüleyici")
        self.setMinimumSize(1000, 800)
        
        # Ana widget ve layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Arama alanı
        search_frame = QFrame()
        search_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                padding: 16px;
            }
        """)
        search_layout = QHBoxLayout(search_frame)
        search_layout.setContentsMargins(16, 16, 16, 16)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Instagram kullanıcı adını girin")
        self.username_input.setMinimumHeight(40)
        self.search_button = QPushButton("Ara")
        self.search_button.setMinimumHeight(40)
        self.search_button.clicked.connect(self.search_profile)
        search_layout.addWidget(self.username_input)
        search_layout.addWidget(self.search_button)
        layout.addWidget(search_frame)
        
        # Scroll area for profile info
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
            }
        """)
        
        # Profile info container
        self.profile_container = QWidget()
        self.profile_layout = QVBoxLayout(self.profile_container)
        self.profile_layout.setSpacing(20)
        scroll.setWidget(self.profile_container)
        layout.addWidget(scroll)
        
        # Status label
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #ed4956; font-size: 14px;")
        layout.addWidget(self.status_label)
        
        # Stil ayarları
        self.setStyleSheet("""
            QMainWindow {
                background-color: #fafafa;
            }
            QLineEdit {
                padding: 8px 16px;
                border: 2px solid #dbdbdb;
                border-radius: 8px;
                font-size: 14px;
                background-color: #fafafa;
            }
            QLineEdit:focus {
                border-color: #0095f6;
            }
            QPushButton {
                padding: 8px 24px;
                background-color: #0095f6;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0086e6;
            }
            QPushButton:disabled {
                background-color: #b2dffc;
            }
            QLabel {
                font-size: 14px;
            }
        """)

    def search_profile(self):
        username = self.username_input.text().strip()
        if not username:
            self.status_label.setText("Lütfen bir kullanıcı adı girin")
            return
            
        self.status_label.setText("Profil bilgileri yükleniyor...")
        self.search_button.setEnabled(False)
        
        # Clear previous results
        for i in reversed(range(self.profile_layout.count())): 
            self.profile_layout.itemAt(i).widget().setParent(None)
        
        # Start worker thread
        self.worker = InstagramWorker(username)
        self.worker.finished.connect(self.display_profile)
        self.worker.error.connect(self.handle_error)
        self.worker.start()

    def display_profile(self, profile_data):
        self.search_button.setEnabled(True)
        self.status_label.setText("")
        
        # Profile header frame
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                padding: 24px;
            }
        """)
        header_layout = QHBoxLayout(header_frame)
        
        # Profile picture
        profile_pic = profile_data['profile_pic']
        profile_pic = profile_pic.resize((150, 150))
        profile_pic.save("temp_profile_pic.jpg")
        
        pic_label = QLabel()
        pixmap = QPixmap("temp_profile_pic.jpg")
        pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pic_label.setPixmap(pixmap)
        pic_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(pic_label)
        
        # Profile information
        info_layout = QVBoxLayout()
        info_layout.setSpacing(8)
        
        # Username and full name
        name_layout = QHBoxLayout()
        name_label = QLabel(f"@{profile_data['username']}")
        name_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        name_layout.addWidget(name_label)
        
        if profile_data['is_verified']:
            verified_label = QLabel("✓")
            verified_label.setStyleSheet("color: #0095f6; font-size: 24px;")
            name_layout.addWidget(verified_label)
        
        info_layout.addLayout(name_layout)
        
        if profile_data['full_name']:
            full_name_label = QLabel(profile_data['full_name'])
            full_name_label.setStyleSheet("font-size: 18px; color: #262626;")
            info_layout.addWidget(full_name_label)
        
        # Stats
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(40)
        
        posts_label = QLabel(f"{profile_data['posts_count']}\nGönderi")
        followers_label = QLabel(f"{profile_data['followers']}\nTakipçi")
        following_label = QLabel(f"{profile_data['following']}\nTakip")
        
        for label in [posts_label, followers_label, following_label]:
            label.setStyleSheet("""
                font-size: 16px;
                font-weight: bold;
                text-align: center;
            """)
            stats_layout.addWidget(label)
        
        info_layout.addLayout(stats_layout)
        
        # Biography
        if profile_data['biography']:
            bio_label = QLabel(profile_data['biography'])
            bio_label.setWordWrap(True)
            bio_label.setStyleSheet("font-size: 14px; color: #262626;")
            info_layout.addWidget(bio_label)
        
        # Business information
        if profile_data['business_category']:
            business_label = QLabel(f"Kategori: {profile_data['business_category']}")
            business_label.setStyleSheet("font-size: 14px; color: #262626;")
            info_layout.addWidget(business_label)
        
        if profile_data['business_email']:
            email_label = QLabel(f"E-posta: {profile_data['business_email']}")
            email_label.setStyleSheet("font-size: 14px; color: #262626;")
            info_layout.addWidget(email_label)
        
        if profile_data['business_phone']:
            phone_label = QLabel(f"Telefon: {profile_data['business_phone']}")
            phone_label.setStyleSheet("font-size: 14px; color: #262626;")
            info_layout.addWidget(phone_label)
        
        # External URL
        if profile_data['external_url']:
            url_label = QLabel(f"Website: {profile_data['external_url']}")
            url_label.setStyleSheet("font-size: 14px; color: #0095f6;")
            info_layout.addWidget(url_label)
        
        # Account status
        if profile_data['is_private']:
            status_label = QLabel("🔒 Gizli Hesap")
            status_label.setStyleSheet("font-size: 14px; color: #262626;")
            info_layout.addWidget(status_label)
        
        header_layout.addLayout(info_layout)
        self.profile_layout.addWidget(header_frame)
        
        # Recent posts section
        if profile_data['recent_posts']:
            posts_frame = QFrame()
            posts_frame.setStyleSheet("""
                QFrame {
                    background-color: white;
                    border-radius: 12px;
                    padding: 24px;
                }
            """)
            posts_layout = QVBoxLayout(posts_frame)
            
            posts_title = QLabel("Son Gönderiler")
            posts_title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 16px;")
            posts_layout.addWidget(posts_title)
            
            posts_grid = QGridLayout()
            posts_grid.setSpacing(16)
            
            for i, post in enumerate(profile_data['recent_posts']):
                post_frame = QFrame()
                post_frame.setStyleSheet("""
                    QFrame {
                        background-color: #fafafa;
                        border-radius: 8px;
                        padding: 12px;
                    }
                """)
                post_layout = QVBoxLayout(post_frame)
                
                # Post image
                if post['image_path'] and os.path.exists(post['image_path']):
                    image_label = QLabel()
                    pixmap = QPixmap(post['image_path'])
                    pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    image_label.setPixmap(pixmap)
                    image_label.setAlignment(Qt.AlignCenter)
                    post_layout.addWidget(image_label)
                elif post['is_video']:
                    video_label = QLabel("🎥 Video Gönderisi")
                    video_label.setStyleSheet("font-size: 14px; color: #262626;")
                    video_label.setAlignment(Qt.AlignCenter)
                    post_layout.addWidget(video_label)
                
                # Post date
                date_label = QLabel(post['date'])
                date_label.setStyleSheet("font-size: 12px; color: #8e8e8e;")
                post_layout.addWidget(date_label)
                
                # Post stats
                stats_label = QLabel(f"❤️ {post['likes']} | 💬 {post['comments']}")
                stats_label.setStyleSheet("font-size: 12px; color: #262626;")
                post_layout.addWidget(stats_label)
                
                # Post caption preview
                if post['caption']:
                    caption_label = QLabel(post['caption'][:100] + "..." if len(post['caption']) > 100 else post['caption'])
                    caption_label.setWordWrap(True)
                    caption_label.setStyleSheet("font-size: 12px; color: #262626;")
                    post_layout.addWidget(caption_label)
                
                posts_grid.addWidget(post_frame, 0, i)
            
            posts_layout.addLayout(posts_grid)
            self.profile_layout.addWidget(posts_frame)
        
        # Clean up temporary files
        if os.path.exists("temp_profile_pic.jpg"):
            os.remove("temp_profile_pic.jpg")
        for i in range(3):
            if os.path.exists(f"temp_post_{i}.jpg"):
                os.remove(f"temp_post_{i}.jpg")

    def handle_error(self, error_message):
        self.search_button.setEnabled(True)
        self.status_label.setText(f"Hata: {error_message}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InstagramViewer()
    window.show()
    sys.exit(app.exec()) 