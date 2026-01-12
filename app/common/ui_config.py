# 应用 UI 配置
from PySide6.QtCore import Qt
from qfluentwidgets import qconfig

# 全局字体配置
FONT_FAMILIES = [
    "Segoe UI",          # Windows 现代UI字体
    "Microsoft YaHei",   # 微软雅黑
    "微软雅黑",          # 微软雅黑中文名
    "Noto Sans CJK SC",  # 跨平台中文字体
    "sans-serif",        # 最后回退到无衬线字体
    "SansSerif",         # 无衬线字体另一个名称
    "SimSun",            # 宋体
]

# 主窗口样式配置
MAIN_WINDOW_STYLES = {
    "dark": {"bg_color": "rgb(28, 28, 28)"},
    "light": {"bg_color": "rgb(255, 255, 255)"},
}

# 标题栏样式配置
TITLE_BAR_STYLES = {
    "dark": {"text_color": "white", "btn_color": Qt.white},
    "light": {"text_color": "black", "btn_color": Qt.black},
}


def apply_font_config():
    """应用全局字体配置"""
    qconfig.fontFamilies.value = FONT_FAMILIES


def get_main_window_style(is_dark: bool) -> dict:
    """获取主窗口样式"""
    return MAIN_WINDOW_STYLES["dark"] if is_dark else MAIN_WINDOW_STYLES["light"]


def get_title_bar_style(is_dark: bool) -> dict:
    """获取标题栏样式"""
    return TITLE_BAR_STYLES["dark"] if is_dark else TITLE_BAR_STYLES["light"]


# 设置卡片样式配置
SETTING_LAYOUT_STYLES = {
    "dark": {
        "border": "1px solid rgb(63, 63, 70)",
        "border_hover": "1px solid rgba(255, 255, 255, 0.12)",
    },
    "light": {
        "border": "1px solid rgb(224, 224, 224)",
        "border_hover": "1px solid rgba(0, 0, 0, 0.2)",
    }
}


def get_setting_layout_style(is_dark: bool) -> dict:
    """获取设置卡片样式"""
    return SETTING_LAYOUT_STYLES["dark"] if is_dark else SETTING_LAYOUT_STYLES["light"]


LOG_TEXT_EDIT_STYLES = {
    "dark": '''
        TextEdit {
            background-color: red;
            border: none;
            border-bottom: none;
        }
        TextEdit:hover {
            background-color: red;
            border-bottom: none;
        }
        TextEdit:focus {
            background-color: red;
            border-bottom: none;
        }
    ''',
    "light": '''
        TextEdit {
            background-color: green;
            border: none;
            border-bottom: none;
        }
        TextEdit:hover {
            background-color: green;
            border-bottom: none;
        }
        TextEdit:focus {
            background-color: green;
            border-bottom: none;
        }
    ''',
}


def get_log_text_edit_qss() -> tuple[str, str]:
    '''Return (light_qss, dark_qss) for the log TextEdit.'''
    return LOG_TEXT_EDIT_STYLES["light"], LOG_TEXT_EDIT_STYLES["dark"]
