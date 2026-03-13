from flask import session

translations = {

    "en": {
        "Select Category": "Select Category",
        "Desktop PC": "Desktop PC",
        "Laptop": "Laptop",
        "Enter Budget": "Enter Budget",
        "Select Use Case": "Select Use Case",
        "Gaming": "Gaming",
        "Video Editing": "Video Editing",
        "Casual Use": "Casual Use",
        "Animation / VFX / Game Dev": "Animation / VFX / Game Dev",
        "Recommended Systems": "Recommended Systems",
        "Performance Explanation": "Performance Explanation",
        "Recommend Again": "Recommend Again",
        "Trending Hardware": "Trending Hardware",
        "Ultimate 4K Gaming GPU": "Ultimate 4K Gaming GPU",
        "High-End 16 Core CPU": "High-End 16 Core CPU",
        "Best 1440p GPU": "Best 1440p GPU",
        "AMD Flagship GPU": "AMD Flagship GPU",
        "Build Your Ultimate Machine": "Build Your Ultimate Machine",
        "AI-powered PC and Laptop recommendations optimized for Gaming, Editing, and Creative Workflows.": "AI-powered PC and Laptop recommendations optimized for Gaming, Editing, and Creative Workflows.",
        "Get Started": "Get Started",
        "Sign in to Continue": "Sign in to Continue",
        "Continue with Google": "Continue with Google",
        "Cancel": "Cancel"
    },

    "ta": {
        "Select Category": "வகையை தேர்ந்தெடுக்கவும்",
        "Desktop PC": "டெஸ்க்டாப் PC",
        "Laptop": "லாப்டாப்",
        "Enter Budget": "பட்ஜெட் உள்ளிடவும்",
        "Select Use Case": "பயன்பாட்டு நோக்கத்தை தேர்ந்தெடுக்கவும்",
        "Gaming": "விளையாட்டு",
        "Video Editing": "வீடியோ திருத்தம்",
        "Casual Use": "சாதாரண பயன்பாடு",
        "Animation / VFX / Game Dev": "அனிமேஷன் / VFX / கேம் டெவலப்மென்ட்",
        "Recommended Systems": "பரிந்துரைக்கப்பட்ட அமைப்புகள்",
        "Performance Explanation": "செயல்திறன் விளக்கம்",
        "Recommend Again": "மீண்டும் பரிந்துரைக்கவும்",
        "Trending Hardware": "பிரபலமான ஹார்ட்வேர்",
        "Ultimate 4K Gaming GPU": "உயர்தர 4K கேமிங் GPU",
        "High-End 16 Core CPU": "உயர்தர 16 கோர் CPU",
        "Best 1440p GPU": "சிறந்த 1440p GPU",
        "AMD Flagship GPU": "AMD முன்னணி GPU",
        "Build Your Ultimate Machine": "உங்கள் சிறந்த கணினியை உருவாக்குங்கள்",
        "AI-powered PC and Laptop recommendations optimized for Gaming, Editing, and Creative Workflows.": "கேமிங், எடிட்டிங் மற்றும் க்ரியேட்டிவ் பணிகளுக்கான AI ஆதரித்த PC மற்றும் Laptop பரிந்துரைகள்.",
        "Get Started": "தொடங்குங்கள்",
        "Sign in to Continue": "தொடர உள்நுழையவும்",
        "Continue with Google": "Google மூலம் தொடரவும்",
        "Cancel": "ரத்து செய்"
    },

    "hi": {
        "Select Category": "श्रेणी चुनें",
        "Desktop PC": "डेस्कटॉप PC",
        "Laptop": "लैपटॉप",
        "Enter Budget": "बजट दर्ज करें",
        "Select Use Case": "उपयोग का प्रकार चुनें",
        "Gaming": "गेमिंग",
        "Video Editing": "वीडियो एडिटिंग",
        "Casual Use": "सामान्य उपयोग",
        "Animation / VFX / Game Dev": "एनीमेशन / VFX / गेम डेवलपमेंट",
        "Recommended Systems": "सुझाए गए सिस्टम",
        "Performance Explanation": "प्रदर्शन विश्लेषण",
        "Recommend Again": "फिर से सुझाव प्राप्त करें",
        "Trending Hardware": "ट्रेंडिंग हार्डवेयर",
        "Ultimate 4K Gaming GPU": "अल्टीमेट 4K गेमिंग GPU",
        "High-End 16 Core CPU": "हाई-एंड 16 कोर CPU",
        "Best 1440p GPU": "सर्वश्रेष्ठ 1440p GPU",
        "AMD Flagship GPU": "AMD फ्लैगशिप GPU",
        "Build Your Ultimate Machine": "अपना सर्वोत्तम सिस्टम बनाएं",
        "AI-powered PC and Laptop recommendations optimized for Gaming, Editing, and Creative Workflows.": "गेमिंग, एडिटिंग और क्रिएटिव वर्क के लिए AI आधारित PC और लैपटॉप सिफारिशें।",
        "Get Started": "शुरू करें",
        "Sign in to Continue": "जारी रखने के लिए साइन इन करें",
        "Continue with Google": "Google के साथ जारी रखें",
        "Cancel": "रद्द करें"
    }
}


def translate(text):
    lang = session.get("lang", "en")
    return translations.get(lang, {}).get(text, text)