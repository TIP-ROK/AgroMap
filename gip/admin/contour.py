from django.contrib.admin.options import TabularInline
from django.contrib.gis import admin
from django.utils.safestring import mark_safe
from leaflet.admin import LeafletGeoAdmin
from simple_history.admin import SimpleHistoryAdmin

from gip.models import Contour
from indexes.models import NDVIIndex


class NDVITabularInline(TabularInline):
    model = NDVIIndex
    readonly_fields = ('id', 'get_html_photo', 'contour', 'date_of_satellite_image', 'get_static_png', 'average_NDVI', 'ndvi_image', )
    fields = ('contour', 'date_of_satellite_image', 'ndvi_image', 'get_html_photo', 'average_NDVI', 'get_static_png', )

    def get_html_photo(self, object):
        if object.ndvi_image:
            return mark_safe(f"<img src='{object.ndvi_image.url}' width=500>")

    def get_static_png(self, obj):
        return mark_safe('''
        <div style="width: 290px;">
          <svg width="100%" height="50" viewBox="0 0 912 72" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="0" width="72" height="72" fill="rgb(0, 91, 76)"/>
          <rect x="72" width="72" height="72" fill="rgb(0, 112, 69)"/>
          <rect x="144" width="72" height="72" fill="rgb(0, 132, 54)"/>
          <rect x="216" width="72" height="72" fill="rgb(0, 151, 30)"/>
          <rect x="288" width="192" height="72" fill="#00AA00"/>
          <rect x="480" width="72" height="72" fill="rgb(60, 184, 34)"/>
          <rect x="552" width="72" height="72" fill="rgb(113, 197, 68)"/>
          <rect x="624" width="72" height="72" fill="rgb(160, 209, 102)"/>
          <rect x="696" width="72" height="72" fill="rgb(198, 221, 136)"/>
          <rect x="768" width="72" height="72" fill="rgb(227, 231, 170)"/>
          <rect x="840" width="72" height="72" fill="rgb(241, 237, 204)"/>
          </svg>
          <div style="display: flex; justify-content: space-between">
            <p style="margin: 0">высокий ndvi</p>
            <p style="margin: 0">низкий ndvi</p>
          </div>
        </div>
        ''')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    get_html_photo.short_description = 'Визуализация NDVI'
    get_static_png.short_description = 'Шкала вегетационного индекса'


@admin.register(Contour)
class ContourAdmin(LeafletGeoAdmin, SimpleHistoryAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at', 'sum_ha')
    list_display = ('id', 'ink', 'conton', 'farmer', )
    list_filter = ('conton', 'farmer', 'sum_ha', )
    ordering = ('conton', 'created_at')
    list_per_page = 20
    search_fields = ('conton__name', 'farmer__pin_inn', 'ink', )
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'ink', )
    inlines = [NDVITabularInline]
