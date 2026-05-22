import flet as ft

def start_sor_launcher(page: ft.Page):
    page.title = 'SoR OS Launcher'
    page.window_width = 390
    page.window_height = 844
    page.bgcolor = '#000000'
    page.padding = 20

    status_bar = ft.Row([
        ft.Text('9:41', color='white', weight='bold', size=14),
        ft.Row([ft.Icon(ft.icons.SIGNAL_CELLULAR_ALT, color='white', size=16), 
                ft.Icon(ft.icons.BATTERY_FULL, color='white', size=16)])
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    app_grid = ft.GridView([
        ft.IconButton(icon=ft.icons.PHONE, icon_color='white', bgcolor='#4CD964', icon_size=28),
        ft.IconButton(icon=ft.icons.MESSAGE, icon_color='white', bgcolor='#007AFF', icon_size=28),
        ft.IconButton(icon=ft.icons.COMPASS_CALIBRATION, icon_color='white', bgcolor='#FF9500', icon_size=28),
        ft.IconButton(icon=ft.icons.SETTINGS, icon_color='white', bgcolor='#8E8E93', icon_size=28)
    ], max_extent=65, spacing=25, run_spacing=25)

    page.add(status_bar, ft.Divider(color='#222222'), app_grid)

if __name__ == '__main__':
    ft.app(target=start_sor_ui if 'start_sor_ui' in globals() else start_sor_launcher)
