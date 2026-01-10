"""编队设置页面 - 替换原有的小工具页面"""

from PySide6.QtWidgets import QFrame
from app.team_setting_card import TeamSettingCard
from app.language_manager import LanguageManager


class TeamSettingInterface(QFrame):
    """编队设置页面，包含20个队伍的配置"""
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("TeamSettingInterface")
        
        # 使用 TeamSettingCard 作为主要内容
        # 默认显示 Team1
        self.team_card = TeamSettingCard(team_num=1, parent=self)
        
        # 设置布局
        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.team_card)
        
        LanguageManager().register_component(self)
    
    def retranslateUi(self):
        """重新翻译UI"""
        self.team_card.retranslateUi()
