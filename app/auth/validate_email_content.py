validate_email_html_content = """
<p>Hello,</p>
<p>You are receiving this email because you need to validate your email in order to activate your account.</p>
<p>
    To confirm your email
    <a href="{{ validate_email_url }}">click here</a>.
</p>
<p>
    Alternatively, you can paste the following link in your browser's address bar: <br>
    {{ validate_email_url }}
</p>
<p>
    Thank you!
</p>
"""