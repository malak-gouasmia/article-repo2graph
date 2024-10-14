# Code from section: Demo
!pip install torch_geometric
!pip install streamlit
!pip install pyngrok
!pip install streamlit-option-menu
!pip install streamlit-lottie

# Code from section: Demo
#Installation de la bibliotheque pycg qui genre les graphe d'appel
!git clone https://github.com/vitsalis/PyCG.git
%cd PyCG
!pip install .


# Code from section: Demo
%cd ..

# Code from section: Demo
!ngrok authtoken 2K5Fn0LG8Miigzi0zMCW2oCoyKd_797ecEbvtBoxk5HCzCcP3

# Code from section: Demo

!pip install scikit-learn==1.3.2


# Code from section: Demo
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Charger les stopwords anglais
stop_words = set(stopwords.words('english'))


# Code from section: Demo
from pyngrok import ngrok

# Authenticate ngrok (if not already done)
ngrok.set_auth_token("2K5Fn0LG8Miigzi0zMCW2oCoyKd_797ecEbvtBoxk5HCzCcP3")

# Start ngrok tunnel to streamlit port
public_url = ngrok.connect(8501)
print(f"Streamlit is available at: {public_url}")


# Code from section: Demo
!streamlit run app.py &>/dev/null&

# Code from section: Demo
from pyngrok import ngrok
tunnels = ngrok.get_tunnels()
print("Active tunnels:", tunnels)

# Code from section: Demo
from pyngrok import ngrok

# Disconnect specific tunnels by their public URLs
ngrok.disconnect("https://38ec-35-229-115-239.ngrok-free.app")
ngrok.disconnect( "https://91ca-35-229-115-239.ngrok-free.app")
ngrok.disconnect( "https://2df8-35-229-115-239.ngrok-free.app")

# Check if the tunnels were disconnected
tunnels = ngrok.get_tunnels()
print("Remaining active tunnels:", tunnels)


