from django.shortcuts import render
import requests

link = "https://www.instagram.com/"
mobile_link = "?utm_medium=copy_link"
web_link = "?utm_source=ig_web_copy_link"
TAIL = "?__a=1"

# > ------------------  GET post ----------------------


def Get_Post(request):
    if request.method == "POST":
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }

        # get message
        PHOTO_URL = request.POST['msg']

        # replace
        Replace_URL = {mobile_link: '?__a=1',
                       web_link: '?__a=1'}

        for key, value in Replace_URL.items():
            PHOTO_URL = PHOTO_URL.replace(key, value)

            """
            response = requests.get(PHOTO_URL, headers=header)
            response.status_code == 404 or 429
            Throw error -> 
            """

        # validation
            # if fields empty or not a correct link if not PHOTO_URL or link or mobile_link or web_link not in PHOTO_URL:
        if not PHOTO_URL or (link or mobile_link or web_link) not in PHOTO_URL:
            Error = "Invalid Link!"
            return render(request, 'home.html', {"Error": Error})

            # output
        else:
            try:
                header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
                }
                response = requests.get(PHOTO_URL, headers=header).json()
                photo = response["graphql"]["shortcode_media"]["display_resources"]
                photo = photo[2]["src"]
                return render(request, 'home.html', {"result": photo})
            except ValueError or KeyError and Exception as e:
                Error = f"Invalid Link! {e}"
                return render(request, 'home.html', {"Error": Error})

    else:
        return render(request, 'home.html')


# > ------------------  GET Video ----------------------


def Get_Videos(request):
    if request.method == "POST":
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }

        # get message
        VIDEO_URL = request.POST['msg']

        # replace
        Replace_URL = {mobile_link: '?__a=1',
                       web_link: '?__a=1'}

        for key, value in Replace_URL.items():
            VIDEO_URL = VIDEO_URL.replace(key, value)

        # validation
            # if fields empty
        if not VIDEO_URL or link not in VIDEO_URL:
            Error = "Invalid Link!"
            return render(request, 'home.html', {"video_Error": Error})

            # output
        else:
            try:
                response = requests.get(VIDEO_URL, headers=header).json()
                VIDEO = response["graphql"]["shortcode_media"]["video_url"]
                return render(request, 'home.html', {"video_result": VIDEO})
            except ValueError or KeyError and Exception as e:
                Error = f"Invalid Link! {e}"
                return render(request, 'home.html', {"video_Error": Error})

    else:
        return render(request, 'home.html')

# > ------------------  GET PROFILE PIC ----------------------


def Get_Profile_Pic(request):
    if request.method == "POST":
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }

        # get message
        USER_NAME = request.POST['msg']

        USERNAME = USER_NAME.replace("@", "")

        PROFILE_USERNAME = link + USERNAME + TAIL

        # validation
        # if fields empty
        if not PROFILE_USERNAME or link not in PROFILE_USERNAME:
            Error = "Invalid Link!"

            return render(request, 'home.html', {"profile_Error": Error})

            # output
        else:
            try:
                response = requests.get(
                    PROFILE_USERNAME, headers=header).json()
                PROFILE_IMG = response["graphql"]["user"]["profile_pic_url_hd"]
                return render(request, 'home.html', {"profile_result": PROFILE_IMG})
            except ValueError or KeyError and Exception as e:
                Error = f"Invalid Link! {e} {PROFILE_USERNAME} {PROFILE_IMG}"
                return render(request, 'home.html', {"profile_Error": Error})

    else:
        return render(request, 'home.html')
