# Vaagdevi Engineering College Website - Django Project

## Project Overview
This is a complete Django-based website for Vaagdevi Engineering College featuring:
- Modern, premium UI design with gradients and animations
- Responsive navigation bar
- Four main pages: Home, About, Courses, and Contact
- Interactive JavaScript features
- Professional CSS styling with design system
- Contact form with validation

## Project Structure
```
myproject/
├── college/
│   ├── static/
│   │   └── college/
│   │       ├── css/
│   │       │   └── style.css
│   │       ├── js/
│   │       │   └── main.js
│   │       └── images/
│   │           ├── logo.png
│   │           ├── campus.png
│   │           └── about.png
│   ├── templates/
│   │   └── college/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── about.html
│   │       ├── courses.html
│   │       └── contact.html
│   ├── views.py
│   └── urls.py
└── myproject/
    ├── settings.py
    └── urls.py
```

## How to Run the Project

1. **Navigate to the project directory:**
   ```bash
   cd d:\myproject\myproject
   ```

2. **Run the Django development server:**
   ```bash
   python manage.py runserver
   ```

3. **Access the website:**
   - Open your browser and go to: `http://127.0.0.1:8000/college/`

## Pages Available

1. **Home Page** - `http://127.0.0.1:8000/college/`
   - Hero section with college introduction
   - Statistics counter animation
   - Feature cards showcasing college highlights
   - Call-to-action section

2. **About Page** - `http://127.0.0.1:8000/college/about/`
   - Mission, Vision, and Values
   - College history and journey
   - Key highlights and achievements
   - Leadership team information

3. **Courses Page** - `http://127.0.0.1:8000/college/courses/`
   - Undergraduate programs (B.Tech)
   - Postgraduate programs (M.Tech)
   - Admission process steps
   - Course specializations

4. **Contact Page** - `http://127.0.0.1:8000/college/contact/`
   - Contact information cards
   - Interactive contact form
   - Map section
   - FAQ section

## Adding Your Name and Department

### IMPORTANT: You MUST update the footer with your personal information!

**Edit the file:** `college/templates/college/base.html`

**Find this section (around line 70-72):**
```html
<p style="margin-top: 0.5rem; font-size: 0.875rem;">
    Developed by: <strong>Your Name</strong> | Department: <strong>Your Department</strong>
</p>
```

**Replace with your actual information:**
```html
<p style="margin-top: 0.5rem; font-size: 0.875rem;">
    Developed by: <strong>John Doe</strong> | Department: <strong>Computer Science Engineering</strong>
</p>
```

## Taking Screenshots for Submission

1. **Run the server:**
   ```bash
   python manage.py runserver
   ```

2. **Open each page in your browser:**
   - Home: `http://127.0.0.1:8000/college/`
   - About: `http://127.0.0.1:8000/college/about/`
   - Courses: `http://127.0.0.1:8000/college/courses/`
   - Contact: `http://127.0.0.1:8000/college/contact/`

3. **Take screenshots:**
   - Press `Windows + Shift + S` to use Snipping Tool
   - Or press `PrtScn` and paste in Paint
   - Make sure your name and department are visible in the footer!
   - Scroll down to capture the footer in at least one screenshot

4. **Save screenshots with descriptive names:**
   - `homepage_screenshot.png`
   - `about_page_screenshot.png`
   - `courses_page_screenshot.png`
   - `contact_page_screenshot.png`

## Features Implemented

### HTML
- Semantic HTML5 structure
- Django template inheritance
- Proper meta tags for SEO
- Accessible form elements

### CSS
- Modern design system with CSS variables
- Gradient backgrounds
- Glassmorphism effects
- Smooth animations and transitions
- Responsive design for mobile devices
- Card-based layouts
- Custom form styling

### JavaScript
- Mobile navigation toggle
- Smooth scrolling
- Intersection Observer for scroll animations
- Counter animations for statistics
- Form validation
- Notification system
- Parallax effects

### Django
- MTV (Model-Template-View) architecture
- URL routing with app namespaces
- Template inheritance
- Static files management
- CSRF protection for forms

## Design Highlights

1. **Premium Aesthetics:**
   - Vibrant gradient color schemes
   - Modern typography (Inter & Poppins fonts)
   - Smooth micro-animations
   - Professional card designs

2. **Interactive Elements:**
   - Hover effects on cards and buttons
   - Animated statistics counters
   - Smooth page transitions
   - Mobile-responsive navigation

3. **User Experience:**
   - Clear navigation structure
   - Intuitive layout
   - Fast loading times
   - Accessible design

## Technologies Used

- **Backend:** Django 5.2.9
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Fonts:** Google Fonts (Inter, Poppins)
- **Icons:** Unicode emoji icons
- **Design:** Custom CSS with modern design patterns

## Submission Checklist

- [ ] Updated footer with your name and department
- [ ] Tested all four pages
- [ ] Taken screenshots of all pages
- [ ] Footer with your name is visible in screenshots
- [ ] All navigation links work correctly
- [ ] Contact form displays properly
- [ ] Website runs without errors

## Support

If you encounter any issues:
1. Make sure Django is installed: `pip install django`
2. Check if the server is running on port 8000
3. Verify all files are in the correct directories
4. Clear browser cache if styling doesn't appear

## Credits

**Developed for:** Vaagdevi Engineering College
**Framework:** Django
**Design:** Modern responsive web design with premium aesthetics

---

**Remember:** Update the footer with your name and department before taking screenshots!
