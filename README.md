# School Management System

A beautiful, modern web-based school management system built with Flask. This application provides an intuitive interface for managing students and teachers with a responsive design.

## Features

- 🎨 **Beautiful Modern UI** - Clean, responsive design with gradient backgrounds and glass-morphism effects
- 👨‍🎓 **Student Management** - Add, view, and search students with detailed information
- 👩‍🏫 **Teacher Management** - Manage teacher profiles with subject information
- 🔍 **Advanced Search** - Search across students and teachers with partial matching
- 📊 **Statistics Dashboard** - View key metrics and statistics
- 📱 **Mobile Responsive** - Works perfectly on all devices
- ⚡ **Fast & Efficient** - Built with Flask for optimal performance

## Screenshots

The application features:
- Modern gradient background with glass-morphism cards
- Beautiful forms with proper validation
- Responsive tables with hover effects
- Interactive navigation with icons
- Real-time statistics and metrics

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## Usage

### Home Page
- View system statistics and quick actions
- Navigate to different sections using the menu

### Adding Students
1. Click "Add New Student" from the menu
2. Fill in the student's name, age, and grade
3. Click "Add Student" to save

### Adding Teachers
1. Click "Add New Teacher" from the menu
2. Enter the teacher's name and select their subject
3. Click "Add Teacher" to save

### Viewing Records
- **Students**: Click "Students" to view all student records
- **Teachers**: Click "Teachers" to view all teacher records
- Both pages show statistics and allow adding new records

### Searching
1. Click "Search" from the menu
2. Enter a name to search for
3. Select whether to search students or teachers
4. View results in a clean table format

## File Structure

```
School_System/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── students.json         # Student data storage
├── teachers.json         # Teacher data storage
├── templates/            # HTML templates
│   ├── base.html         # Base template with styling
│   ├── index.html        # Home page
│   ├── add_student.html  # Add student form
│   ├── add_teacher.html  # Add teacher form
│   ├── students.html     # Students list page
│   ├── teachers.html     # Teachers list page
│   └── search.html       # Search page
└── school.py             # Original console application (backup)
```

## Features in Detail

### Student Management
- **Name**: Full name of the student
- **Age**: Must be between 1-25 years
- **Grade**: Select from Kindergarten to 12th Grade
- **Validation**: All fields are required with proper validation

### Teacher Management
- **Name**: Full name of the teacher
- **Subject**: Select from a comprehensive list of subjects
- **Validation**: All fields are required

### Search Functionality
- **Case-insensitive**: Search works regardless of case
- **Partial matching**: Find results with partial names
- **Filtered results**: Search specifically in students or teachers
- **Clean display**: Results shown in organized tables

### Responsive Design
- **Mobile-friendly**: Works on phones, tablets, and desktops
- **Modern styling**: Gradient backgrounds and glass effects
- **Smooth animations**: Hover effects and transitions
- **Accessible**: Proper contrast and readable fonts

## Technical Details

- **Framework**: Flask 2.3.3
- **Styling**: Custom CSS with modern design principles
- **Icons**: Font Awesome 6.0
- **Data Storage**: JSON files for simplicity
- **Validation**: Server-side form validation
- **Responsive**: CSS Grid and Flexbox for layout

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Future Enhancements

Potential improvements for future versions:
- User authentication and roles
- Database integration (SQLite/PostgreSQL)
- File upload for student/teacher photos
- Grade tracking and academic records
- Attendance management
- Report generation
- API endpoints for mobile apps

## Support

If you encounter any issues or have questions:
1. Check that all dependencies are installed correctly
2. Ensure Python 3.7+ is being used
3. Verify that the JSON files have proper permissions
4. Check the console for any error messages

## License

This project is open source and available under the MIT License. 