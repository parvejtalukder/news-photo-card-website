from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os
from io import BytesIO

app = Flask(__name__)

# Create a folder to store images (if not exists)
if not os.path.exists('static/images'):
    os.makedirs('static/images')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input
        title = request.form['title']
        description = request.form['description']
        news_image = request.files['news_image']
        logo_image = request.files['logo_image']
        
        # Save images
        news_image_path = os.path.join('static/images', news_image.filename)
        logo_image_path = os.path.join('static/images', logo_image.filename)
        news_image.save(news_image_path)
        logo_image.save(logo_image_path)
        
        # Open images using Pillow
        news_img = Image.open(news_image_path)
        logo_img = Image.open(logo_image_path)
        
        # Example: Resize the images if necessary (you can customize)
        logo_img = logo_img.resize((100, 100))  # Resize the logo
        
        # Add text (title and description) to the image
        # For simplicity, just adding text here; you can create a custom layout
        from PIL import ImageDraw, ImageFont
        draw = ImageDraw.Draw(news_img)
        font = ImageFont.load_default()
        
        # Adding title and description
        draw.text((10, 10), title, font=font, fill="white")
        draw.text((10, 40), description, font=font, fill="white")
        
        # Save the final card
        final_card_path = os.path.join('static/images', 'final_card.png')
        news_img.save(final_card_path)
        
        return render_template('preview.html', title=title, description=description, final_card_path=final_card_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
