import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import re
from datetime import datetime

class EmailSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Sender Pro")
        self.root.geometry("900x1000")
        self.root.configure(bg='#f0f0f0')
        
        # Set icon and style
        self.root.resizable(False, False)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.success_color = "#27ae60"
        self.error_color = "#e74c3c"
        self.warning_color = "#f39c12"
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main title
        title_label = tk.Label(
            self.root,
            text="📧 Email Sender Pro",
            font=("Arial", 24, "bold"),
            fg=self.primary_color,
            bg='#f0f0f0'
        )
        title_label.pack(pady=20)
        
        # Main container
        main_container = tk.Frame(self.root, bg='white', relief='raised', bd=2)
        main_container.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Email configuration section
        config_frame = tk.LabelFrame(main_container, text="Email Configuration", font=("Arial", 12, "bold"), bg='white')
        config_frame.pack(padx=20, pady=10, fill='x')
        
        # Sender email
        tk.Label(config_frame, text="From Email:", font=("Arial", 10, "bold"), bg='white').grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.sender_email = tk.Entry(config_frame, font=("Arial", 10), width=40)
        self.sender_email.grid(row=0, column=1, padx=10, pady=5)
        self.sender_email.insert(0, "vishwastiwari1901@gmail.com")
        
        # App password
        tk.Label(config_frame, text="App Password:", font=("Arial", 10, "bold"), bg='white').grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.app_password = tk.Entry(config_frame, font=("Arial", 10), width=40, show="*")
        self.app_password.grid(row=1, column=1, padx=10, pady=5)
        self.app_password.insert(0, "irzlzsfuzndlqgks")
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(padx=20, pady=20, fill='both', expand=True)
        
        # Single email tab
        self.single_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.single_frame, text="Single Email")
        self.create_single_email_tab()
        
        # Bulk email tab
        self.bulk_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.bulk_frame, text="Bulk Email")
        self.create_bulk_email_tab()
        
        # Status section
        status_frame = tk.Frame(main_container, bg='white')
        status_frame.pack(padx=20, pady=10, fill='x')
        
        # Status label
        self.status_label = tk.Label(
            status_frame,
            text="Ready to send emails",
            font=("Arial", 10, "bold"),
            fg=self.success_color,
            bg='white'
        )
        self.status_label.pack(side='left')
        
        # Email progress counter
        self.email_progress_label = tk.Label(
            status_frame,
            text="",
            font=("Arial", 10, "bold"),
            fg=self.secondary_color,
            bg='white'
        )
        self.email_progress_label.pack(side='left', padx=(20, 0))
        
        # Progress bar
        self.progress = ttk.Progressbar(status_frame, mode='determinate', length=200)
        self.progress.pack(side='right', padx=(10, 0))
        
        # Time label
        self.time_label = tk.Label(
            status_frame,
            text=f"Last updated: {datetime.now().strftime('%H:%M:%S')}",
            font=("Arial", 8),
            fg='gray',
            bg='white'
        )
        self.time_label.pack(side='right', padx=(0, 10))
        
    def create_single_email_tab(self):
        # Recipient section
        recipient_frame = tk.LabelFrame(self.single_frame, text="Recipient", font=("Arial", 10, "bold"))
        recipient_frame.pack(padx=20, pady=10, fill='x')
        
        self.recipient_email = tk.Entry(recipient_frame, font=("Arial", 10), width=50)
        self.recipient_email.pack(padx=10, pady=10, fill='x')
        self.recipient_email.insert(0, "fuelgo123@gmail.com")
        
        # Email content section - limit height to leave space for buttons
        content_frame = tk.LabelFrame(self.single_frame, text="Email Content", font=("Arial", 10, "bold"))
        content_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Set maximum height for content to ensure buttons are visible
        content_frame.pack_propagate(False)
        content_frame.configure(height=250)
        
        # Create a canvas with scrollbar for the content
        canvas = tk.Canvas(content_frame)
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Subject
        tk.Label(scrollable_frame, text="Subject:", font=("Arial", 10, "bold")).pack(anchor='w', padx=10, pady=(10, 5))
        self.subject_entry = tk.Entry(scrollable_frame, font=("Arial", 10), width=50)
        self.subject_entry.pack(padx=10, pady=(0, 10), fill='x')
        self.subject_entry.insert(0, "Test Email")
        
        # Message
        tk.Label(scrollable_frame, text="Message:", font=("Arial", 10, "bold")).pack(anchor='w', padx=10, pady=(10, 5))
        self.message_text = scrolledtext.ScrolledText(scrollable_frame, height=6, font=("Arial", 10))
        self.message_text.pack(padx=10, pady=(0, 10), fill='both', expand=True)
        self.message_text.insert('1.0', "This is a test email sent from Email Sender Pro!")
        
        # Buttons - ensure they're always visible at bottom
        button_frame = tk.Frame(self.single_frame, bg='white', relief='raised', bd=2)
        button_frame.pack(side='bottom', pady=15, fill='x', padx=20)
        
        # Add a spacer to push buttons to bottom
        spacer = tk.Frame(self.single_frame, height=20)
        spacer.pack(side='bottom', fill='x')
        
        # Send button
        self.send_button = tk.Button(
            button_frame,
            text="📤 Send Email",
            command=self.send_single_email,
            font=("Arial", 12, "bold"),
            bg=self.secondary_color,
            fg='white',
            relief='raised',
            bd=2,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.send_button.pack(side='left', padx=10)
        
        # Clear button
        self.clear_button = tk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_single_fields,
            font=("Arial", 12, "bold"),
            bg='#95a5a6',
            fg='white',
            relief='raised',
            bd=2,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.clear_button.pack(side='left', padx=10)
        
    def create_bulk_email_tab(self):
        # Recipients section
        recipients_frame = tk.LabelFrame(self.bulk_frame, text="Recipients", font=("Arial", 10, "bold"))
        recipients_frame.pack(padx=20, pady=10, fill='x')
        
        # Instructions
        instructions = tk.Label(
            recipients_frame,
            text="Paste email addresses from Excel (one per line or separated by commas):",
            font=("Arial", 9),
            fg='gray'
        )
        instructions.pack(anchor='w', padx=10, pady=(10, 5))
        
        # Email addresses text area
        self.bulk_emails_text = scrolledtext.ScrolledText(recipients_frame, height=6, font=("Arial", 10))
        self.bulk_emails_text.pack(padx=10, pady=(0, 10), fill='x')
        self.bulk_emails_text.insert('1.0', "example1@gmail.com\nexample2@gmail.com\nexample3@gmail.com")
        
        # Email count label
        self.email_count_label = tk.Label(
            recipients_frame,
            text="Valid emails: 0",
            font=("Arial", 10, "bold"),
            fg=self.success_color
        )
        self.email_count_label.pack(anchor='w', padx=10, pady=(0, 10))
        
        # Email content section - limit height to leave space for buttons
        bulk_content_frame = tk.LabelFrame(self.bulk_frame, text="Email Content", font=("Arial", 10, "bold"))
        bulk_content_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Set maximum height for content to ensure buttons are visible
        bulk_content_frame.pack_propagate(False)
        bulk_content_frame.configure(height=250)
        
        # Create a canvas with scrollbar for the bulk content
        bulk_canvas = tk.Canvas(bulk_content_frame)
        bulk_scrollbar = ttk.Scrollbar(bulk_content_frame, orient="vertical", command=bulk_canvas.yview)
        bulk_scrollable_frame = tk.Frame(bulk_canvas)
        
        bulk_scrollable_frame.bind(
            "<Configure>",
            lambda e: bulk_canvas.configure(scrollregion=bulk_canvas.bbox("all"))
        )
        
        bulk_canvas.create_window((0, 0), window=bulk_scrollable_frame, anchor="nw")
        bulk_canvas.configure(yscrollcommand=bulk_scrollbar.set)
        
        bulk_canvas.pack(side="left", fill="both", expand=True)
        bulk_scrollbar.pack(side="right", fill="y")
        
        # Subject
        tk.Label(bulk_scrollable_frame, text="Subject:", font=("Arial", 10, "bold")).pack(anchor='w', padx=10, pady=(10, 5))
        self.bulk_subject_entry = tk.Entry(bulk_scrollable_frame, font=("Arial", 10), width=50)
        self.bulk_subject_entry.pack(padx=10, pady=(0, 10), fill='x')
        self.bulk_subject_entry.insert(0, "Bulk Test Email")
        
        # Message
        tk.Label(bulk_scrollable_frame, text="Message:", font=("Arial", 10, "bold")).pack(anchor='w', padx=10, pady=(10, 5))
        self.bulk_message_text = scrolledtext.ScrolledText(bulk_scrollable_frame, height=4, font=("Arial", 10))
        self.bulk_message_text.pack(padx=10, pady=(0, 10), fill='both', expand=True)
        self.bulk_message_text.insert('1.0', "This is a bulk email sent from Email Sender Pro!")
        
        # Bulk email options
        options_frame = tk.Frame(bulk_scrollable_frame)
        options_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        self.delay_var = tk.BooleanVar(value=True)
        self.delay_check = tk.Checkbutton(
            options_frame,
            text="Add delay between emails (recommended)",
            variable=self.delay_var,
            font=("Arial", 9)
        )
        self.delay_check.pack(side='left')
        
        # Buttons frame - ensure it's always visible at bottom
        bulk_button_frame = tk.Frame(self.bulk_frame, bg='white', relief='raised', bd=2)
        bulk_button_frame.pack(side='bottom', pady=15, fill='x', padx=20)
        
        # Add a spacer to push buttons to bottom
        bulk_spacer = tk.Frame(self.bulk_frame, height=20)
        bulk_spacer.pack(side='bottom', fill='x')
        
        # Send bulk button
        self.send_bulk_button = tk.Button(
            bulk_button_frame,
            text="📬 Send Bulk Email",
            command=self.send_bulk_email,
            font=("Arial", 12, "bold"),
            bg=self.warning_color,
            fg='white',
            relief='raised',
            bd=2,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.send_bulk_button.pack(side='left', padx=10)
        
        # Validate emails button
        self.validate_button = tk.Button(
            bulk_button_frame,
            text="✅ Validate Emails",
            command=self.validate_bulk_emails,
            font=("Arial", 12, "bold"),
            bg=self.success_color,
            fg='white',
            relief='raised',
            bd=2,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.validate_button.pack(side='left', padx=10)
        
        # Clear bulk button
        self.clear_bulk_button = tk.Button(
            bulk_button_frame,
            text="🗑️ Clear",
            command=self.clear_bulk_fields,
            font=("Arial", 12, "bold"),
            bg='#95a5a6',
            fg='white',
            relief='raised',
            bd=2,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.clear_bulk_button.pack(side='left', padx=10)
        
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def parse_email_list(self, email_text):
        """Parse email addresses from text (supports newlines and commas)"""
        emails = []
        for line in email_text.split('\n'):
            for email in line.split(','):
                email = email.strip()
                if email and self.validate_email(email):
                    emails.append(email)
        return emails
    
    def validate_bulk_emails(self):
        """Validate and count bulk email addresses"""
        email_text = self.bulk_emails_text.get('1.0', tk.END).strip()
        if not email_text:
            messagebox.showwarning("Warning", "Please enter email addresses!")
            return
        
        valid_emails = self.parse_email_list(email_text)
        self.email_count_label.config(text=f"Valid emails: {len(valid_emails)}")
        
        if valid_emails:
            messagebox.showinfo("Validation Result", f"Found {len(valid_emails)} valid email addresses!")
        else:
            messagebox.showwarning("Validation Result", "No valid email addresses found!")
    
    def send_single_email(self):
        """Send single email"""
        sender = self.sender_email.get().strip()
        password = self.app_password.get().strip()
        recipient = self.recipient_email.get().strip()
        subject = self.subject_entry.get().strip()
        message = self.message_text.get('1.0', tk.END).strip()
        
        if not all([sender, password, recipient, subject, message]):
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        if not self.validate_email(sender):
            messagebox.showerror("Error", "Invalid sender email format!")
            return
        
        if not self.validate_email(recipient):
            messagebox.showerror("Error", "Invalid recipient email format!")
            return
        
        # Disable send button and show progress
        self.send_button.config(state='disabled', text="Sending...")
        self.progress['value'] = 0
        self.progress['maximum'] = 1
        self.status_label.config(text="Sending email...", fg=self.secondary_color)
        self.email_progress_label.config(text="1/1 emails")
        
        # Run email sending in separate thread
        thread = threading.Thread(target=self._send_email_thread, args=(sender, password, [recipient], subject, message, False))
        thread.daemon = True
        thread.start()
    
    def send_bulk_email(self):
        """Send bulk emails"""
        sender = self.sender_email.get().strip()
        password = self.app_password.get().strip()
        email_text = self.bulk_emails_text.get('1.0', tk.END).strip()
        subject = self.bulk_subject_entry.get().strip()
        message = self.bulk_message_text.get('1.0', tk.END).strip()
        
        if not all([sender, password, email_text, subject, message]):
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        if not self.validate_email(sender):
            messagebox.showerror("Error", "Invalid sender email format!")
            return
        
        # Parse and validate recipient emails
        recipients = self.parse_email_list(email_text)
        if not recipients:
            messagebox.showerror("Error", "No valid email addresses found!")
            return
        
        # Confirm bulk sending
        confirm = messagebox.askyesno(
            "Confirm Bulk Send",
            f"Are you sure you want to send this email to {len(recipients)} recipients?\n\n"
            "This action cannot be undone!"
        )
        
        if not confirm:
            return
        
        # Disable send button and show progress
        self.send_bulk_button.config(state='disabled', text="Sending...")
        self.progress['value'] = 0
        self.progress['maximum'] = len(recipients)
        self.status_label.config(text=f"Sending bulk email to {len(recipients)} recipients...", fg=self.warning_color)
        self.email_progress_label.config(text=f"0/{len(recipients)} emails sent")
        
        # Run bulk email sending in separate thread
        thread = threading.Thread(target=self._send_email_thread, args=(sender, password, recipients, subject, message, self.delay_var.get()))
        thread.daemon = True
        thread.start()
    
    def _send_email_thread(self, sender, password, recipients, subject, message, use_delay=False):
        """Send email(s) in background thread"""
        import time
        
        try:
            # Create SMTP session
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            
            # Login
            server.login(sender, password)
            
            success_count = 0
            failed_count = 0
            failed_emails = []
            
            for i, recipient in enumerate(recipients):
                try:
                    # Create message
                    msg = MIMEMultipart()
                    msg['From'] = sender
                    msg['To'] = recipient
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))
                    
                    # Send email
                    text = msg.as_string()
                    server.sendmail(sender, recipient, text)
                    success_count += 1
                    
                    # Update status and progress
                    if len(recipients) > 1:
                        self.root.after(0, lambda: self.update_progress(success_count, len(recipients)))
                    
                    # Add delay between emails if requested
                    if use_delay and i < len(recipients) - 1:
                        time.sleep(2)  # 2 second delay
                        
                except Exception as e:
                    failed_count += 1
                    failed_emails.append(f"{recipient}: {str(e)}")
            
            server.quit()
            
            # Update GUI on main thread
            if len(recipients) == 1:
                self.root.after(0, self._email_sent_success)
            else:
                self.root.after(0, self._bulk_email_sent_success, success_count, failed_count, failed_emails)
            
        except smtplib.SMTPAuthenticationError:
            self.root.after(0, self._email_sent_error, "Authentication failed!\n\nPlease check:\n• Your email address is correct\n• You're using an App Password (not regular password)\n• 2-Factor Authentication is enabled\n• The App Password is correct")
        except Exception as e:
            self.root.after(0, self._email_sent_error, f"Error sending email:\n{str(e)}")
    
    def update_progress(self, current, total):
        """Update progress bar and email counter"""
        self.progress['value'] = current
        self.email_progress_label.config(text=f"{current}/{total} emails sent")
        self.root.update_idletasks()
    
    def _email_sent_success(self):
        """Handle successful single email sending"""
        self.progress['value'] = 1
        self.send_button.config(state='normal', text="📤 Send Email")
        self.status_label.config(text="Email sent successfully!", fg=self.success_color)
        self.email_progress_label.config(text="1/1 emails sent")
        self.time_label.config(text=f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
        messagebox.showinfo("Success", "Email sent successfully!")
    
    def _bulk_email_sent_success(self, success_count, failed_count, failed_emails):
        """Handle successful bulk email sending"""
        total_emails = success_count + failed_count
        self.progress['value'] = total_emails
        self.send_bulk_button.config(state='normal', text="📬 Send Bulk Email")
        self.time_label.config(text=f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
        
        if failed_count == 0:
            self.status_label.config(text=f"All {success_count} emails sent successfully!", fg=self.success_color)
            self.email_progress_label.config(text=f"{success_count}/{success_count} emails sent")
            messagebox.showinfo("Success", f"All {success_count} emails sent successfully!")
        else:
            self.status_label.config(text=f"{success_count} sent, {failed_count} failed", fg=self.warning_color)
            self.email_progress_label.config(text=f"{total_emails}/{total_emails} emails processed")
            
            # Show detailed error message
            error_msg = f"Successfully sent: {success_count}\nFailed: {failed_count}\n\n"
            if failed_emails:
                error_msg += "Failed emails:\n" + "\n".join(failed_emails[:5])  # Show first 5 errors
                if len(failed_emails) > 5:
                    error_msg += f"\n... and {len(failed_emails) - 5} more"
            
            messagebox.showwarning("Bulk Send Complete", error_msg)
    
    def _email_sent_error(self, error_message):
        """Handle email sending error"""
        self.progress['value'] = 0
        self.send_button.config(state='normal', text="📤 Send Email")
        self.send_bulk_button.config(state='normal', text="📬 Send Bulk Email")
        self.status_label.config(text="Failed to send email", fg=self.error_color)
        self.email_progress_label.config(text="")
        self.time_label.config(text=f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
        messagebox.showerror("Error", error_message)
    
    def clear_single_fields(self):
        """Clear single email fields"""
        self.subject_entry.delete(0, tk.END)
        self.subject_entry.insert(0, "Test Email")
        self.message_text.delete('1.0', tk.END)
        self.message_text.insert('1.0', "This is a test email sent from Email Sender Pro!")
        self.status_label.config(text="Ready to send emails", fg=self.success_color)
        self.email_progress_label.config(text="")
        self.progress['value'] = 0
        self.time_label.config(text=f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
    
    def clear_bulk_fields(self):
        """Clear bulk email fields"""
        self.bulk_emails_text.delete('1.0', tk.END)
        self.bulk_emails_text.insert('1.0', "example1@gmail.com\nexample2@gmail.com\nexample3@gmail.com")
        self.bulk_subject_entry.delete(0, tk.END)
        self.bulk_subject_entry.insert(0, "Bulk Test Email")
        self.bulk_message_text.delete('1.0', tk.END)
        self.bulk_message_text.insert('1.0', "This is a bulk email sent from Email Sender Pro!")
        self.email_count_label.config(text="Valid emails: 0")
        self.status_label.config(text="Ready to send emails", fg=self.success_color)
        self.email_progress_label.config(text="")
        self.progress['value'] = 0
        self.time_label.config(text=f"Last updated: {datetime.now().strftime('%H:%M:%S')}")

def main():
    root = tk.Tk()
    app = EmailSenderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

