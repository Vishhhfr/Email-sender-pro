# 📧 Email Sender Pro

A beautiful and user-friendly GUI application for sending emails using Gmail SMTP. Built with Python and tkinter.

## ✨ Features

- 🎨 Modern and intuitive user interface with tabbed design
- 📧 Easy email composition with rich text support
- 📬 **Bulk email sending** - Send to multiple recipients at once
- 📋 **Excel integration** - Paste email columns directly from Excel
- 🔒 Secure authentication using Gmail App Passwords
- ✅ Real-time email validation and counting
- 📊 Progress indicators and status updates
- 🚀 Multi-threaded email sending (no GUI freezing)
- 🛡️ Comprehensive error handling
- ⏱️ **Smart delays** - Prevent spam detection with configurable delays

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Gmail account with 2-Factor Authentication enabled
- Gmail App Password

### Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd email-sender-pro
   ```

2. **Install required packages** (if any)
   ```bash
   pip install -r requirements.txt
   ```
   
   *Note: This application uses only Python built-in libraries, so no additional installation is required!*

3. **Run the application**
   ```bash
   python emailsend.py
   ```

## 🔧 Gmail Setup

### Step 1: Enable 2-Factor Authentication
1. Go to your Google Account settings
2. Navigate to Security
3. Enable 2-Step Verification

### Step 2: Generate App Password
1. Go to Google Account settings
2. Navigate to Security → 2-Step Verification
3. Click on "App passwords"
4. Select "Mail" and your device
5. Copy the generated 16-character password

### Step 3: Use in Application
- Enter your Gmail address in "From Email"
- Enter the App Password (not your regular Gmail password) in "App Password"

## 📖 How to Use

### Single Email Mode
1. **Launch the application**
   - Double-click `emailsend.py` or run from command line

2. **Configure email settings**
   - Enter your Gmail address
   - Enter your Gmail App Password

3. **Switch to "Single Email" tab**
   - Enter recipient's email address
   - Add a subject line
   - Write your message in the text area

4. **Send the email**
   - Click "📤 Send Email" button
   - Wait for confirmation message

### Bulk Email Mode
1. **Switch to "Bulk Email" tab**
   - Paste email addresses from Excel (one per line or comma-separated)
   - Click "✅ Validate Emails" to check and count valid addresses

2. **Compose your bulk email**
   - Add a subject line
   - Write your message (same content for all recipients)

3. **Configure sending options**
   - Enable/disable delay between emails (recommended to prevent spam detection)

4. **Send bulk emails**
   - Click "📬 Send Bulk Email" button
   - Confirm the action
   - Monitor progress and results

## 🎯 Features Explained

### Email Validation
- Automatically validates email format
- Ensures all required fields are filled
- Provides clear error messages
- **Bulk validation** - Count and validate multiple email addresses at once

### Bulk Email Features
- **Excel integration** - Copy-paste email columns directly from Excel
- **Flexible input** - Supports newline-separated or comma-separated email lists
- **Smart delays** - Configurable delays between emails to prevent spam detection
- **Progress tracking** - Real-time updates on bulk sending progress
- **Error reporting** - Detailed feedback on failed deliveries

### Security Features
- Uses Gmail App Passwords for secure authentication
- Password field is masked for privacy
- No credentials are stored locally
- **Rate limiting** - Built-in delays prevent account restrictions

### User Experience
- **Tabbed interface** - Easy switching between single and bulk modes
- Progress bar shows sending status
- Real-time status updates
- Clear success/error messages
- Non-blocking interface (GUI doesn't freeze)

## 🛠️ Troubleshooting

### Common Issues

**Authentication Error (535)**
- Ensure you're using an App Password, not your regular Gmail password
- Verify 2-Factor Authentication is enabled
- Check that your email address is correct

**Connection Issues**
- Check your internet connection
- Ensure Gmail SMTP is not blocked by firewall
- Try using a different network

**Email Not Received**
- Check recipient's spam folder
- Verify recipient email address is correct
- Ensure your Gmail account is not restricted

**Bulk Email Issues**
- Use delays between emails to prevent spam detection
- Limit bulk sends to reasonable numbers (50-100 per session)
- Verify all email addresses before sending
- Check Gmail sending limits (500/day for regular accounts)

### Error Messages

| Error | Solution |
|-------|----------|
| "Authentication failed" | Use App Password instead of regular password |
| "Invalid email format" | Check email address format |
| "Connection timeout" | Check internet connection |
| "SMTP server error" | Try again later or check Gmail status |
| "No valid emails found" | Check email list format and validation |
| "Bulk send confirmation" | Confirm you want to send to multiple recipients |

## 🔒 Security Notes

- **Never share your App Password**
- **Don't commit credentials to version control**
- **Use App Passwords instead of regular passwords**
- **Enable 2-Factor Authentication on your Gmail account**

## 📝 Customization

You can easily customize the application:

### Colors
Edit the color variables in the `__init__` method:
```python
self.primary_color = "#2c3e50"
self.secondary_color = "#3498db"
self.success_color = "#27ae60"
self.error_color = "#e74c3c"
```

### Window Size
Change the geometry in the `__init__` method:
```python
self.root.geometry("600x700")
```

### Default Values
Modify the default email addresses and messages in `create_widgets()`.

## 🤝 Contributing

Feel free to contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Python and tkinter
- Uses Gmail SMTP for email delivery
- Inspired by the need for a simple, secure email sender

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the error messages carefully
3. Ensure your Gmail setup is correct
4. Create an issue in the repository

---

**Happy Email Sending! 📧✨** 