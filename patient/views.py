from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import gradio,openai
# Create your views here.

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(username, password, user)
        # Check if authentication successful
        if user is not None:
            try:
                login(request, user)
                return redirect('index')
            
            except:
                messages.error(request, 'Invalid username and/or password.')
                return redirect('register')
            
        else:
            messages.error(request, 'Invalid username and/or password.')
            return redirect('login')
    else:
        return render(request, "login.html")
    


def logout_view(request):
    logout(request)
    return redirect('index')



def register(request):
    if request.method == "POST":
            username = request.POST["username"]
            password=request.POST["password"]
            print(username, password)

            try:
                user = User.objects.create_user(username, password)
                user.save()           

            except:
                messages.error(request, '"Username already taken"')
                return redirect('register')
            messages.success(request, 'Patient registered successfully!')
            return redirect('login')
    else:
            return render(request, "register.html")
    


def land(request):
    return render(request, 'index.html')


def chatbot(request):
    
    openai.api_key = "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"

    messages = [{"role": "system", "content": "You are a licensed Drug Counselor"}]


    def CustomChatGPT(user_input):
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
            max_tokens=130,
            
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply

    demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Assessment Bot")
    gradio_ui = demo.launch(share=True)

    return render(request, 'chatbot.html', {'gradio_ui': gradio_ui})
