# Supplier_to_Magento.py
# An excel file containing the columns for Magento import and each supplier mapping
# is read into a DataFrame.
# The supplier data is then mapped accordingly.
# If the import file changes then edit the import_header file.
# The supplier_name must be edited for each import

import csv
import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)


#  ****  EDIT THIS LINE ONLY  ****
# THS MUST MATCH THE COLUMN HEADER IN THE EXCEL FILE
supplier_name = "BIZ"

supplier_file = supplier_name + ".csv"
magento_filename = "Magento_" + supplier_name + ".csv"

# *** IMPORTANT FILE ***
df = pd.read_excel("Import_Suppliers.xlsx")
mapping = df.set_index('MAGENTO')[supplier_name].to_dict()
# MAGENTO is column name
# supplier_name is column name

# create holder for import headers
import_headers = []

# get the headers for import file
with open('import_headers_R1.csv' ,'r') as headers:
    reader = csv.reader(headers)
    for row in reader:
        import_headers.append(row)


in_file = open(supplier_file, 'r',encoding='utf-8')
reader = csv.DictReader(in_file)

out_file = open(magento_filename, 'w',newline="", encoding="utf8")
writer = csv.DictWriter(out_file ,fieldnames=import_headers[0])

writer.writeheader()

for row in reader:
    writer.writerow({
        "sku": row.get(mapping["sku"]),
        "store_view_code": row.get(mapping["store_view_code"]),
        "attribute_set_code": row.get(mapping["attribute_set_code"]),
        "product_type": row.get(mapping["product_type"]),
        "categories": row.get(mapping["categories"]),
        "product_websites": row.get(mapping["product_websites"]),
        "name": row.get(mapping["name"]),
        "description": row.get(mapping["description"]),
        "short_description": row.get(mapping["short_description"]),
        "weight": row.get(mapping["weight"]),
        "product_online": row.get(mapping["product_online"]),
        "tax_class_name": row.get(mapping["tax_class_name"]),
        "visibility": row.get(mapping["visibility"]),
        "price": row.get(mapping["price"]),
        "special_price": row.get(mapping["special_price"]),
        "special_price_from_date": row.get(mapping["special_price_from_date"]),
        "special_price_to_date": row.get(mapping["special_price_to_date"]),
        "url_key": row.get(mapping["url_key"]),
        "meta_title": row.get(mapping["meta_title"]),
        "meta_keywords": row.get(mapping["meta_keywords"]),
        "meta_description": row.get(mapping["meta_description"]),
        "base_image": row.get(mapping["base_image"]),
        "base_image_label": row.get(mapping["base_image_label"]),
        "small_image": row.get(mapping["small_image"]),
        "small_image_label": row.get(mapping["small_image_label"]),
        "thumbnail_image": row.get(mapping["thumbnail_image"]),
        "thumbnail_image_label": row.get(mapping["thumbnail_image_label"]),
        "swatch_image": row.get(mapping["swatch_image"]),
        "swatch_image_label": row.get(mapping["swatch_image_label"]),
        "created_at": row.get(mapping["created_at"]),
        "updated_at": row.get(mapping["updated_at"]),
        "new_from_date": row.get(mapping["new_from_date"]),
        "new_to_date": row.get(mapping["new_to_date"]),
        "display_product_options_in": row.get(mapping["display_product_options_in"]),
        "map_price": row.get(mapping["map_price"]),
        "msrp_price": row.get(mapping["msrp_price"]),
        "map_enabled": row.get(mapping["map_enabled"]),
        "gift_message_available": row.get(mapping["gift_message_available"]),
        "custom_design": row.get(mapping["custom_design"]),
        "custom_design_from": row.get(mapping["custom_design_from"]),
        "custom_design_to": row.get(mapping["custom_design_to"]),
        "custom_layout_update": row.get(mapping["custom_layout_update"]),
        "page_layout": row.get(mapping["page_layout"]),
        "product_options_container": row.get(mapping["product_options_container"]),
        "msrp_display_actual_price_type": row.get(mapping["msrp_display_actual_price_type"]),
        "country_of_manufacture": row.get(mapping["country_of_manufacture"]),
        "carton_height": row.get(mapping["carton_height"]),
        "carton_depth": row.get(mapping["carton_depth"]),
        "carton_width": row.get(mapping["carton_width"]),
        "carton_weight": row.get(mapping["carton_weight"]),
        "carton_qty": row.get(mapping["carton_qty"]),
        "carton_cubic": row.get(mapping["carton_cubic"]),
        "carton_notes": row.get(mapping["carton_notes"]),
        "freight_description": row.get(mapping["freight_description"]),
        "size": row.get(mapping["size"]),
        "branded": row.get(mapping["branded"]),
        "climate": row.get(mapping["climate"]),
        "color": row.get(mapping["color"]),
        "decoration_areas": row.get(mapping["decoration_areas"]),
        "decoration_options_available": row.get(mapping["decoration_options_available"]),
        "decoration_type": row.get(mapping["decoration_type"]),
        "material": row.get(mapping["material"]),
        "manufacturer": row.get(mapping["manufacturer"]),
        "pattern": row.get(mapping["pattern"]),
        "featured": row.get(mapping["featured"]),
        "catalogue_name": row.get(mapping["catalogue_name"]),
        "indent_only": row.get(mapping["indent_only"]),
        "price_decoration_description": row.get(mapping["price_decoration_description"]),
        "product_features": row.get(mapping["product_features"]),
        "supplier_product_url": row.get(mapping["supplier_product_url"]),
        "markup_per": row.get(mapping["markup_per"]),
        "product_packaging_inner": row.get(mapping["product_packaging_inner"]),
        "seller": row.get(mapping["seller"]),
        "additional_attributes": row.get(mapping["additional_attributes"]),
        "qty": row.get(mapping["qty"]),
        "out_of_stock_qty": row.get(mapping["out_of_stock_qty"]),
        "use_config_min_qty": row.get(mapping["use_config_min_qty"]),
        "is_qty_decimal": row.get(mapping["is_qty_decimal"]),
        "allow_backorders": row.get(mapping["allow_backorders"]),
        "use_config_backorders": row.get(mapping["use_config_backorders"]),
        "min_cart_qty": row.get(mapping["min_cart_qty"]),
        "use_config_min_sale_qty": row.get(mapping["use_config_min_sale_qty"]),
        "max_cart_qty": row.get(mapping["max_cart_qty"]),
        "use_config_max_sale_qty": row.get(mapping["use_config_max_sale_qty"]),
        "is_in_stock": row.get(mapping["is_in_stock"]),
        "notify_on_stock_below": row.get(mapping["notify_on_stock_below"]),
        "use_config_notify_stock_qty": row.get(mapping["use_config_notify_stock_qty"]),
        "manage_stock": row.get(mapping["manage_stock"]),
        "use_config_manage_stock": row.get(mapping["use_config_manage_stock"]),
        "use_config_qty_increments": row.get(mapping["use_config_qty_increments"]),
        "qty_increments": row.get(mapping["qty_increments"]),
        "use_config_enable_qty_inc": row.get(mapping["use_config_enable_qty_inc"]),
        "enable_qty_increments": row.get(mapping["enable_qty_increments"]),
        "is_decimal_divided": row.get(mapping["is_decimal_divided"]),
        "website_id": row.get(mapping["website_id"]),
        "related_skus": row.get(mapping["related_skus"]),
        "related_position": row.get(mapping["related_position"]),
        "crosssell_skus": row.get(mapping["crosssell_skus"]),
        "crosssell_position": row.get(mapping["crosssell_position"]),
        "upsell_skus": row.get(mapping["upsell_skus"]),
        "upsell_position": row.get(mapping["upsell_position"]),
        "additional_images": row.get(mapping["additional_images"]),
        "additional_image_labels": row.get(mapping["additional_image_labels"]),
        "hide_from_product_page": row.get(mapping["hide_from_product_page"]),
        "custom_options": row.get(mapping["custom_options"]),
        "bundle_price_type": row.get(mapping["bundle_price_type"]),
        "bundle_sku_type": row.get(mapping["bundle_sku_type"]),
        "bundle_price_view": row.get(mapping["bundle_price_view"]),
        "bundle_weight_type": row.get(mapping["bundle_weight_type"]),
        "bundle_values": row.get(mapping["bundle_values"]),
        "bundle_shipment_type": row.get(mapping["bundle_shipment_type"]),
        "configurable_variations": row.get(mapping["configurable_variations"]),
        "configurable_variation_labels": row.get(mapping["configurable_variation_labels"]),
        "associated_skus": row.get(mapping["associated_skus"])
    })

in_file.close() # data stored in memory NB: If large files may need to do row by row
out_file.close()
