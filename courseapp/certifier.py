from PIL import Image, ImageDraw, ImageFont
import os

def certifier(name, course, date):
    # Load image
    base_dir = os.path.dirname(os.path.abspath(__file__)).split('courseapp')[0]
    template_path = os.path.join(base_dir, 'assets/img/certificate template.jpg')
    print(template_path)
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Load font
    font_path=os.path.join(base_dir, 'assets/fonts/font.ttf')
    print(font_path)
    fontName = ImageFont.truetype(font_path, 80)
    fontCourse = ImageFont.truetype(font_path, 40)
    fontDate = ImageFont.truetype(font_path, 30)
    coursesz = draw.textlength(course, font=fontCourse)
    namesz = draw.textlength(name, font=fontName)
    w  = img.width
    h = img.height
    draw.text(((w-namesz)/2+100, 300), name, fill='black', font=fontName, align='center')
    draw.text(((w-coursesz)/2+100, 400), course, fill='black', font=fontCourse)
    draw.text((475, h-180), date.strftime('%Y-%m-%d'), fill='black', font=fontDate)

    # Save image
    os.makedirs(os.path.join(base_dir, 'media/certificates'), exist_ok=True)
    img.save(os.path.join(base_dir, f'media/certificates/{name}_{course}.jpg'))
    return os.path.join(base_dir, f'media/certificates/{name}_{course}.jpg')

if __name__ == '__main__':
    certifier('John Doe', 'Python Programming', '2021-01-01')