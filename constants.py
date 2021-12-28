# test


# File path
REF_PATH = "C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\1 Important Configs\\Python Reference Folder\\"

SUPP_PATH = "C:\\Users\\Dean\\Dropbox\\Brand Elevate\\6 Website\\1 Important Configs\\Supplier Data Files\\"

RESULTS_PATH = "C:\\Users\\Dean\\Test Out Files\\"

PATH_IMG = "C:\\Users\\Dean\\OneDrive\\Business\\Supplier Data\\Legend Life\\Appa File Images\\"

# Dictionary mapping Brand Elevate codes to the colours
BE_CLUT = {'WH':'white',
           'GY':'gray',
           'SI':'silver',
           'BK':'black',
           'MA':'maroon',
           'RD':'red',
           'PU':'purple',
           'PK':'pink',
           'GR':'green',
           'LGR':'light green',
           'OL':'olive',
           'YE':'yellow',
           'NA':'navy',
           'BL':'blue',
           'AQ':'aqua',
           'OR':'orange',
           'BR':'brown',
           'LBR':'light brown',
           'CR':'cream',
           'CH':'charcoal'}


"""
AVAILABLE DECORATION OPTIONS BRAND ELEVATE

'Plastisol Transfer',
'Sublimation',
'Screen Print',
'Laser Etch',
'Digital Transfer',
'Embroidery',
"""
# Legend Life categores to Brand Elevate mapping
LEGEND_BE_CATS = {
    'TEES': 'T-SHIRTS',
    'CORPORATE CASUAL': 'CASUAL',
    'SPORTS AND DUFFLES': 'SPORTS BAGS',
    'WET WEATHER/ACTIVEWEAR':'SPORTS',
    'EXPRESS HEADWEAR':'HEADWEAR',
    'POLO SHIRTS':'POLOS',
    'STOCK UMBRELLAS':'UMBRELLAS',
    'SCHOOL HEADWEAR':'SCHOOL',
    'NON WOVEN':'CONFERENCE & EXPO'
    }

CAT_DOUBLES = ['TECHNOLOGY','ACCESSORIES','MEN','LADIES']

# updated 17-01-2017
MAGENTO_HEADERS = [
    'sku','store_view_code','attribute_set_code','product_type','categories','product_websites','name',
   'description','short_description','weight','product_online','tax_class_name','visibility','price',
   'special_price','special_price_from_date','special_price_to_date','url_key','meta_title',
   'meta_keywords','meta_description','base_image','base_image_label','small_image','small_image_label',
   'thumbnail_image','thumbnail_image_label','swatch_image','swatch_image_label','created_at',
   'updated_at','new_from_date','new_to_date','display_product_options_in','map_price','msrp_price',
   'map_enabled','gift_message_available','custom_design','custom_design_from','custom_design_to',
   'custom_layout_update','page_layout','product_options_container','msrp_display_actual_price_type',
   'country_of_manufacture','carton_height','carton_depth','carton_width','carton_weight','carton_qty',
   'carton_cubic','carton_notes','freight_description','size','branded','climate','color',
   'decoration_areas','decoration_options_available','decoration_type','manufacturer',
   'pattern','featured','catalogue_name','indent_only','price_decoration_description','product_features',
   'supplier_product_url','markup_per','product_packaging_inner','seller','gender','product_material',
   'additional_attributes','qty','out_of_stock_qty','use_config_min_qty','is_qty_decimal',
   'allow_backorders','use_config_backorders','min_cart_qty','use_config_min_sale_qty','max_cart_qty',
   'use_config_max_sale_qty','is_in_stock','notify_on_stock_below','use_config_notify_stock_qty',
   'manage_stock','use_config_manage_stock','use_config_qty_increments','qty_increments',
   'use_config_enable_qty_inc','enable_qty_increments','is_decimal_divided','website_id','related_skus',
   'related_position','crosssell_skus','crosssell_position','upsell_skus','upsell_position',
   'additional_images','additional_image_labels','hide_from_product_page','custom_options',
   'bundle_price_type','bundle_sku_type','bundle_price_view','bundle_weight_type','bundle_values',
   'bundle_shipment_type','configurable_variations','configurable_variation_labels','associated_skus']

# Set duplicate fields
# copies field values that are the same.  Saves doing it after manipulating one of the fields
# SET_EQUAL_FIELDS_DIC = {
#     'meta_title':'name',
#     'meta_description':'description'
# }

# update 17-01-2017
# The following has the default values set for all suppliers.  These defaults can be overwritten furing runtime
# if required.
MAGENTO_IMPORT_DIC = {
    'sku': None,                                # required
    'store_view_code': None,
    'attribute_set_code': 'Default',
    'product_type': None,                       # simple,configurable
    'categories': None,                         # Default Category/Gear|Default Category/Gear/Bags
    'product_websites': 'base',
    'name': None,                               # product name or basic description
    'description': None,                        # description
    'short_description': None,                  # short description
    'weight': 1,
    'product_online': 1,
    'tax_class_name': 'Taxable Goods',
    'visibility': None,                         # depends on simple or configurable
    'price': None,
    'special_price': None,
    'special_price_from_date': None,
    'special_price_to_date': None,
    'url_key': None,                            # product name without spaces e.g. trendy-jumper
    'meta_title': None,                         # AUTO name
    'meta_keywords': None,                      # AUTO mapped
    'meta_description': None,                   # AUTO description
    'base_image': None,                         # need to work out and set
    'base_image_label': None,
    'small_image': None,                        # AUTO
    'small_image_label': None,
    'thumbnail_image': None,                    # AUTO
    'thumbnail_image_label': None,
    'swatch_image': None,
    'swatch_image_label': None,
    'created_at': None,
    'updated_at': None,
    'new_from_date': None,
    'new_to_date': None,
    'display_product_options_in': 'Block after Info Column',
    'map_price': None,
    'msrp_price': None,
    'map_enabled': None,
    'gift_message_available': None,
    'custom_design': None,
    'custom_design_from': None,
    'custom_design_to': None,
    'custom_layout_update': None,
    'page_layout': None,
    'product_options_container': None,
    'msrp_display_actual_price_type': None,
    'country_of_manufacture': None,
    'carton_height': None,
    'carton_depth': None,
    'carton_width': None,
    'carton_weight': None,
    'carton_qty': None,
    'carton_cubic': None,
    'carton_notes': None,
    'freight_description': None,
    'size': None,                               # need to set
    'branded': None,
    'climate': None,
    'color': None,
    'decoration_areas': None,
    'decoration_options_available': None,
    'decoration_type': None,
    'manufacturer': None,
    'pattern': None,
    'featured': 0,
    'catalogue_name': None,
    'indent_only': None,
    'price_decoration_description': None,
    'product_features': None,
    'supplier_product_url': None,
    'markup_per': 40,                           # default set to 40% but best set during runtime
    'product_packaging_inner': None,
    'seller': None,
    'gender': None,
    'product_material': None,
    'additional_attributes': None,
    'qty': 100000,                                # default to stop showing out of stock
    'out_of_stock_qty': 0,
    'use_config_min_qty': 1,
    'is_qty_decimal': 0,
    'allow_backorders': 0,
    'use_config_backorders': 1,
    'min_cart_qty': None,
    'use_config_min_sale_qty': 1,
    'max_cart_qty': 10000,
    'use_config_max_sale_qty': 1,
    'is_in_stock': 1,
    'notify_on_stock_below': 1,
    'use_config_notify_stock_qty': 1,
    'manage_stock': 1,
    'use_config_manage_stock': 1,
    'use_config_qty_increments': 1,
    'qty_increments': 1,
    'use_config_enable_qty_inc': 1,
    'enable_qty_increments': 0,
    'is_decimal_divided': 0,
    'website_id': 0,
    'related_skus': None,
    'related_position': None,
    'crosssell_skus': None,
    'crosssell_position': None,
    'upsell_skus': None,
    'upsell_position': None,
    'additional_images': None,
    'additional_image_labels': None,
    'hide_from_product_page': None,
    'custom_options': None,
    'bundle_price_type': None,
    'bundle_sku_type': None,
    'bundle_price_view': None,
    'bundle_weight_type': None,
    'bundle_values': None,
    'bundle_shipment_type': None,
    'configurable_variations': None,
    'configurable_variation_labels': None,
    'associated_skus': None
    }

ADV_PRICING_HEADERS = \
    ['sku','tier_price_website','tier_price_customer_group','tier_price_qty','tier_price']

ADV_PRICING_DIC={
    'sku':None,
    'tier_price_website':None,
    'tier_price_customer_group':None,
    'tier_price_qty':None,
    'tier_price':None
}