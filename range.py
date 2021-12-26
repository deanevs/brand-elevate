
# legend_map is a dictionary mapping fields direct through to the Magento import.

RANGE_MAP = {
    #'product_code':'sku',
    # '':'store_view_code',
    # 'Default':'attribute_set_code',
    # '':'product_type',
    # 'categorisation':'categories',
    # 'base':'product_websites',
    # 'product_name':'name',
    #'product_description':'description',
    #'':'short_description',
    #####'product_features':'short_description',
    # '1':'weight',
    # '1':'product_online',
    # 'Taxable Goods':'tax_class_name',
    # '':'visibility',
    'price_1':'price',
    # '':'special_price',
    # '':'special_price_from_date',
    # '':'special_price_to_date',
    # 'sku':'url_key',
    'product_name':'meta_title',
    ########'additional_keywords':'meta_keywords'
    #'':'meta_keywords',
    #'product_description':'meta_description',
    # 'product_image_file_name':'base_image',
    # '':'base_image_label',
    # 'product_image_file_name':'small_image',
    # '':'small_image_label',
    # 'product_image_file_name':'thumbnail_image',
    # '':'thumbnail_image_label',
    # 'product_image_file_name':'swatch_image',
    # '':'swatch_image_label',
    # '':'created_at',
    # '':'updated_at',
    # '':'new_from_date',
    # '':'new_to_date',
    # 'Block after Info Column':'display_product_options_in',
    # '':'map_price',
    # '':'msrp_price',
    # '':'map_enabled',
    # '':'gift_message_available',
    # '':'custom_design',
    # '':'custom_design_from',
    # '':'custom_design_to',
    # '':'custom_layout_update',
    # '':'page_layout',
    # '':'product_options_container',
    # '':'msrp_display_actual_price_type',
    # '':'country_of_manufacture',
    'carton_height':'carton_height',
    'carton_depth':'carton_depth',
    'carton_width':'carton_width',
    'carton_weight':'carton_weight',
    'carton_qty':'carton_qty',
    'carton_cubic':'carton_cubic',
    # '':'carton_notes',
    'freight_description':'freight_description',
    # 'product_sizes':'size',
    'branded':'branded',
    # '':'climate',
    # 'colours_available_supplier':'color',
    'decoration_areas':'decoration_areas',
    'decoration_options_available':'decoration_options_available',
    'decoration_type':'decoration_type',
    'label_name':'manufacturer',
    # '':'pattern',
    # '0':'featured',
    'catalogue_name':'catalogue_name',
    #'indent_only':'indent_only',
    'price_decoration_description':'price_decoration_description',
    # '':'product_features',
    'product_URL':'supplier_product_url',
    # '40':'markup_per',
    # '':'product_packaging_inner',
    'brand_name':'seller',
    # '':'gender',
    # 'product_materials':'product_material',
    # '':'additional_attributes',
    # '1000':'qty',
    'discontinued_stock':'out_of_stock_qty',
    # '1':'use_config_min_qty',
    # '0':'is_qty_decimal',
    # '0':'allow_backorders',
    # '1':'use_config_backorders',
    'MOQ':'min_cart_qty',
    # '1':'use_config_min_sale_qty',
    # '10000':'max_cart_qty',
    # '1':'use_config_max_sale_qty',
    # '1':'is_in_stock',
    # '':'notify_on_stock_below',
    # '1':'use_config_notify_stock_qty',
    # '1':'manage_stock',
    # '1':'use_config_manage_stock',
    # '1':'use_config_qty_increments',
    # '2':'qty_increments',
    # '1':'use_config_enable_qty_inc',
    # '0':'enable_qty_increments',
    # '0':'is_decimal_divided',
    # '0':'website_id',
    # '':'related_skus',
    # '':'related_position',
    # '':'crosssell_skus',
    # '':'crosssell_position',
    # '':'upsell_skus',
    # '':'upsell_position',
    #'alternate_views_image_file_names':'additional_images',
    # '':'additional_image_labels',
    # '':'hide_from_product_page',
    # '':'custom_options',
    # '':'bundle_price_type',
    # '':'bundle_sku_type',
    # '':'bundle_price_view',
    # '':'bundle_weight_type',
    # '':'bundle_values',
    # '':'bundle_shipment_type',
    # '':'configurable_variations',
    # '':'configurable_variation_labels',
    # '':'associated_skus'
    }


def set_fields():
    # set('sku', product_code)
    set('store_view_code', '')
    set('attribute_set_code', 'Default')
    # set('product_type', )
    set('categories', category_subcategory)
    set('product_websites', 'base')
    # set('name', product_name)
    set('description', product_description)
    set('short_description', )
    set('weight', 1)
    set('product_online', 0)
    set('tax_class_name', 'Taxable Goods')
    # set('visibility', '')
    set('price', price_1)
    set('special_price', '')
    set('special_price_from_date', '')
    set('special_price_to_date', '')
    # set('url_key', '')
    set('meta_title', '')
    set('meta_keywords', additional_keywords)
    set('meta_description', '')
    # set('base_image', product_image_file_name)
    set('base_image_label', '')
    # set('small_image', '')
    set('small_image_label', '')
    # set('thumbnail_image', '')
    set('thumbnail_image_label', '')
    set('swatch_image', '')
    set('swatch_image_label', '')
    set('created_at', '')
    set('updated_at', '')
    set('new_from_date', '')
    set('new_to_date', '')
    set('display_product_options_in', 'Block after Info Column')
    set('map_price', '')
    set('msrp_price', '')
    set('map_enabled', '')
    set('gift_message_available', '')
    set('custom_design', '')
    set('custom_design_from', '')
    set('custom_design_to', '')
    set('custom_layout_update', '')
    set('page_layout', '')
    set('product_options_container', '')
    set('msrp_display_actual_price_type', '')
    set('country_of_manufacture', '')
    set('carton_height', carton_height)
    set('carton_depth', carton_depth)
    set('carton_width', carton_width)
    set('carton_weight', carton_weight)
    set('carton_qty', carton_qty)
    set('carton_cubic', carton_cubic)
    set('carton_notes', carton_notes)
    set('freight_description', freight_description)
    set('size', product_sizes)
    set('branded', branded)
    set('climate', '')
    set('color', colours_available_supplier)
    set('decoration_areas', decoration_areas)
    set('decoration_options_available', decoration_options_available)
    set('decoration_type', decoration_type)
    set('manufacturer', brand_name)
    set('pattern', '')
    set('featured', 0)
    set('catalogue_name', catalogue_name)
    set('indent_only', indent_only)
    set('price_decoration_description', price_decoration_description)
    set('product_features', )
    set('supplier_product_url', product_URL)
    set('markup_per', 40)
    set('product_packaging_inner', '')
    set('seller', member_supplier_name)
    set('gender', gender_return)
    set('product_material', product_materials)
    set('additional_attributes', '')
    set('qty', 1000)
    set('out_of_stock_qty', discontinued_stock)
    set('use_config_min_qty', 1)
    set('is_qty_decimal', 0)
    set('allow_backorders', 0)
    set('use_config_backorders', 1)
    set('min_cart_qty', MOQ)
    set('use_config_min_sale_qty', 1)
    set('max_cart_qty', 10000)
    set('use_config_max_sale_qty', 1)
    set('is_in_stock', 1)
    set('notify_on_stock_below', '')
    set('use_config_notify_stock_qty', 1)
    set('manage_stock', 1)
    set('use_config_manage_stock', 1)
    set('use_config_qty_increments', 1)
    set('qty_increments', 2)
    set('use_config_enable_qty_inc', 1)
    set('enable_qty_increments', 0)
    set('is_decimal_divided', 0)
    set('website_id', 0)
    set('related_skus', '')
    set('related_position', '')
    set('crosssell_skus', '')
    set('crosssell_position', '')
    set('upsell_skus', '')
    set('upsell_position', '')
    set('additional_images', alternate_views_image_file_names)
    set('additional_image_labels', '')
    set('hide_from_product_page', '')
    set('custom_options', '')
    set('bundle_price_type', '')
    set('bundle_sku_type', '')
    set('bundle_price_view', '')
    set('bundle_weight_type', '')
    set('bundle_values', '')
    set('bundle_shipment_type', '')
    # set('configurable_variations', )
    set('configurable_variation_labels', '')
    set('associated_skus', '')


member_supplier_name = row['member_supplier_name'],
membership_number = row['membership_number'],
catalogue_name = row['catalogue_name'],
brand_name = row['brand_name'],
label_name = row['label_name'],
appa_product_code = row['appa_product_code'],
product_code = row['product_code'],
product_name = row['product_name'],
product_code_group = row['product_code_group'],
category_ /_sub category = row['category_ /_sub category'],
additional_keywords = row['additional_keywords'],
product_tags = row['product_tags'],
discontinued_stock = row['discontinued_stock'],
product_description = row['product_description'],
description_additional = row['description_additional'],
product_features = row['product_features'],
product_materials = row['product_materials'],
product_item_size = row['product_item_size'],
product_packaging_inner = row['product_packaging_inner'],
product_image_file_name = row['product_image_file_name'],
alternate_views_image_file_names = row['alternate_views_image_file_names'],
group_image_file_name = row['group_image_file_name'],
colours_available_appa = row['colours_available_appa'],
colours_available_supplier = row['colours_available_supplier'],
colour_image_file_names = row['colour_image_file_names'],
colour_product_codes = row['colour_product_codes'],
product_sizes = row['product_sizes'],
size_images = row['size_images'],
size_product_code = row['size_product_code'],
decoration_options_available = row['decoration_options_available'],
decoration_areas = row['decoration_areas'],
indent_only = row['indent_only'],
branded = row['branded'],
custom_field_1 = row['custom_field_1'],
custom_field_2 = row['custom_field_2'],
custom_field_3 = row['custom_field_3'],
price_decoration_description = row['price_decoration_description'],
price_by_size = row['price_by_size'],
price_by_colour = row['price_by_colour'],
decoration_type = row['decoration_type'],
price_product_code = row['price_product_code'],
price_notes = row['price_notes'],
MOQ = row['MOQ'],
IOQ = row['IOQ'],
qty_1 = row['qty_1'],
price_1 = row['price_1'],
qty_2 = row['qty_2'],
price_2 = row['price_2'],
qty_3 = row['qty_3'],
price_3 = row['price_3'],
qty_4 = row['qty_4'],
price_4 = row['price_4'],
qty_5 = row['qty_5'],
price_5 = row['price_5'],
qty_6 = row['qty_6'],
price_6 = row['price_6'],
qty_7 = row['qty_7'],
price_7 = row['price_7'],
qty_8 = row['qty_8'],
price_8 = row['price_8'],
additional_charges_name1 = row['additional_charges_name1'],
additional_charge_value1 = row['additional_charge_value1'],
additional_charges_notes1 = row['additional_charges_notes1'],
additional_charges_name2 = row['additional_charges_name2'],
additional_charge_value2 = row['additional_charge_value2'],
additional_charges_notes2 = row['additional_charges_notes2'],
carton_height = row['carton_height'],
carton_width = row['carton_width'],
carton_depth = row['carton_depth'],
carton_weight = row['carton_weight'],
carton_qty = row['carton_qty'],
carton_cubic = row['carton_cubic'],
carton_notes = row['carton_notes'],
freight_description = row['freight_description'],
product_URL = row['product_URL'],



RANGE_CLUT = ({
    'ABS Plastic':'GY',
    'Aust - Black':'BK',
    'Beige':'CR',
    'Black':'BK',
    'Black Solid':'BK',
    'Black with Blue detail':'BK',
    'Black with blue':'BK',
    'Blue':'BL',
    'Blue (2728)':'BL',
    'Blue (2756)':'BL',
    'Blue (280)':'BL',
    'Blue (285)':'BL',
    'Blue (286)':'BL',
    'Blue (293)':'BL',
    'Blue (2935)':'BL',
    'Blue (294)':'BL',
    'Blue (295)':'BL',
    'Blue (534)':'BL',
    'Blue (Process Blue)':'BL',
    'Blue (REFLXE BLUE)':'BL',
    'Champagne':'CR',
    'Charcoal + Orange':'GY',
    'Clear':'CL',
    'Graphite':'GY',
    'Green':'GR',
    'Green (380)':'GR',
    'Green (381)':'GR',
    'Green (390)':'GR',
    'Grey':'GY',
    'Grey (429)':'GY',
    'Grey (Cool Grey 10)':'GY',
    'Grey (Cool Grey 11)':'GY',
    'Lime Green':'LGR',
    'NZ - White only':'WH',
    'Natural':'CR',
    'Navy':'NA',
    'Orange':'OR',
    'Pale Blue':'AQ',
    'Pink (496)':'PK',
    'Platinum Grey':'GY',
    'Purple':'PU',
    'Red':'RD',
    'Red (185)':'RD',
    'Red (185C)':'RD',
    'Red (186)':'RD',
    'Red (187)':'RD',
    'Red (192)':'RD',
    'Red (1925)':'RD',
    'Red (193)':'RD',
    'Red (1945)':'RD',
    'Red Natural':'RD',
    'Reflex Blue':'BL',
    'Reflex Bue':'BL',
    'Royal':'BL',
    'Royal Blue':'BL',
    'Silver':'SI',
    'Silver with Black detail':'SI',
    'Terracotta':'LBR',
    'Transparent':'CL',
    'White':'WH',
    'Yellow':'YE',
    'Yellow (107)':'YE',
    'clear':'CL',
    'red':'RD',
    'red or yellow inside':'RD',
    'white':'WH'
})



