import markdown

with open('/home/ubuntu/investigacion_branding_mejorada.md', 'r', encoding='utf-8') as f:
    markdown_text = f.read()

html = markdown.markdown(markdown_text)

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investigación de Branding Visual</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; background-color: #f4f4f4; color: #333; }}
        .container {{ max-width: 900px; margin: auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1, h2, h3, h4, h5, h6 {{ color: #0056b3; }}
        a {{ color: #007bff; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
        table, th, td {{ border: 1px solid #ddd; }}
        th, td {{ padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        blockquote {{ border-left: 5px solid #ccc; margin: 1.5em 10px; padding: 0.5em 10px; color: #666; }}
    </style>
</head>
<body>
    <div class="container">
        {html}
    </div>
</body>
</html>
'''

with open('/home/ubuntu/website_output/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
