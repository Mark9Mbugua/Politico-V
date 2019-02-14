from urllib.parse import urlparse

class LogoUrlValidator:

    def validate_logo_url(self, logoUrl):
        result = True    
        parsed_url = urlparse(logoUrl)

        if not isinstance(logoUrl, str):
            result = {'Error': 'logoUrl should be in string format', 'Status': 400}

        if logoUrl == "" or logoUrl.isspace():
            result = {'Error': 'logoUrl is required', 'Status': 400}

        if not parsed_url.scheme:
            result = {'Error': "logoUrl should be in the format 'https://www.twitter.com/profile/img.jpg'", 'Status': 400 }

        if not parsed_url.netloc:
            result = {'Error': "logoUrl should be in the format 'https://www.twitter.com/profile/img.jpg'", 'Status': 400 }
        
        if not parsed_url.path:
            result = {'Error': "logoUrl should be in the format 'https://www.twitter.com/profile/img.jpg'", 'Status': 400 }

        return result