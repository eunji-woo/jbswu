from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(
        request,
        'problem/index.html',
    )
# ------------------------------------------------------------
def article(request, number):
    if number == 1:
        result = article1(request)
        return result
    elif number == 2:
        result = article2(request)
        return result
    elif number == 3:
        result = article3(request)
        return result
    
def article1(request):
    res_data = {}
    items = ["‘소개딩’ 그룹 개바리 SNS에 올린 글… 보아니와 불화설 증거?",
            "작성자: 박윤진 (작성일 2021.08.28)",
            "불화설 증거로 추측되는 게시글/사진=개바리 SNS",
            "‘소개딩’ 그룹 개바리가 일주일만에 처음으로 SNS에 글을 게재했다.",
            "개바리는 지난 22일, 평소 친하게 지내던 같은 그룹 보아니와 함께 무대를 하던 중, 다리를 다친 보아니의 다리를 보고 농담을 던졌다.",
            "이를 시작으로 SNS와 커뮤니티 등지에서 개바리가 보아니를 그룹에서 의도적으로 배제하고 있다고 주장하는 글들이 올라왔다.",
            "개중에는 개바리의 데뷔 초기 자작곡 ”G의 마음“이라는 곡이 보아니를 저격하고 있다고 재조명받고 있다.",
            "”G의 마음“은 개바리의 연습생 생활을 담은 곡으로, 따라부르기 쉬운 멜로디와 담담한 가사로 발매 당시 음원 차트를 석권하는 등 센세이션한 열풍을 일으켰다.",
            "XX는 26일 오후, 자신의 SNS 질문과 답변에 “어떻게 모든 사람을 좋아하겠어요.”라고 답했다.",
            "네티즌들은 ”헐ㅋㅋ어쩐지 쎄하더라.“, ”어떻게 다친 애한테 그럴수가 있어? 관상은 못속여.“, 등의 반응을 보였다.",]
    res_data['items'] = items

    if request.method == 'POST':
        user = request.user
        profile = request.user.profile
        profile.score4 = "1"
        profile.save()
        return redirect('../../main')

    return render(request, 'problem/article1.html', res_data)

def article2(request):
    res_data = {}
    items = ["백신 바꿔치기? 백신 바꿔치기 목격했다는 SNS 이용자",
             "작성자: 기사지망생 우은지 (작성일 2021.08.28)",
            "한 페이스북 이용자가 백신을 바꿔치기 하는 모습을 목격했다는 글이 온라인 커뮤니티를 비롯한 다양한 SNS에 퍼졌다.",
            "백신 바꿔치기를 목격했다는 페이스북 이용자는 “잔여백신 맞고 오는 길인데 화이자 명찰 달고 있는 사람한테 아스트라제네카 백신 약물 가져가는 거 봄. 뭐지? 나도 내가 신청한 백신 종류말고 다른 종류 백신 맞은건 아니겠지? 무서워 ㅠ..” 라는 글을 게시했다.",
            "이에 커뮤니티, SNS 사용자들은 “진짜임?”, “백신 무서워서 못 맞겠다.”, “근데 작게 쓰여져 있는 백신 이름을 어떻게 봐?ㅋㅋㅋ” 등의 반응을 보이고 있다.",]
    res_data['items'] = items
    

    if request.method == 'POST':
        user = request.user
        profile = request.user.profile
        profile.score5 = "1"
        profile.save()
        return redirect('../../main')

    return render(request, 'problem/article2.html', res_data)

def article3(request):
    res_data = {}
    items = ["의류 브랜드 '소개딩' 브랜드 평판 9월.. 1위 기업 상승세 '개바리 보아니' 상품 품절대란",
             "작성자: 신지혜 (작성일 2021.07.26)",
             "한국기업평판 연구소 빅데이터 분석결과 2위 훨라 3위 F&Z…",
            "섬유의류 상장기업 브랜드 평판 2020년 9월 빅데이터 분석결과 1위 소개딩 2위 훨라 3위 F&Z 순으로 분석되었다.",
            "한국기업평판연구소는 국내 섬유의류 상장기업에 대한 브랜드 빅데이터 평판을 분석하였다. 섬유 의류 상장기업 브랜드 빅데이터 27,328,611개를 분석하였다.",
            "브랜드에 대한 평판은 브랜드에 대한 소비자들의 활동 빅데이터를 참여가치, 소통가치, 소셜가치, 시장가치, 재무가치로 나누게 된다. 섬유 의류 상장기업 브랜드 평판 지수는 참여지수, 미디어지수, 소통지수, 커뮤니티지수, 시장지수, 사회공헌지수로 분석하였다.",
            "2020년 9월 1위, 소개딩 브랜드는 참여지수 253,964 미디어지수 17,213 소통지수 324,256 등으로 지난 2월 브랜드 평판과 비교하여 2.44%상승하였다.",
            "2위, 훨라 브랜드는 참여지수 212,454 미디어지수 15,234 소통지수 312,455등으로 지난 2월 브랜드 평판과 비교하여 1.86%상승하였다.",
            "3위, F&Z 브랜드는 참여지수 199.566 미디어지수 14,212 소통지수 298,875등으로 지난 2월 브랜드 평판과 비교하여 0.87%감소하였다.",
            "의류 브랜드 '소개딩'은 브랜드 평판 9월 1위로 2021년에도 계속 상승세를 보일것으로 추측한다.",
            "'소개딩'의 대표 제품으로는 '개바리 보아니'티셔츠로 알려져 있다. 품절대란을 예상하고 만든 티셔츠로 '개바리 보아니'티셔츠는 '소개딩'홈페이지에서 바로 구매 가능하다.",
            ]
    res_data['items'] = items
    

    if request.method == 'POST':
        user = request.user
        profile = request.user.profile
        profile.score6 = "1"
        profile.save()
        return redirect('../../main')

    return render(request, 'problem/article3.html', res_data)
# ------------------------------------------------------------
def literacy(request, number):
    if number == 1:
        result = literacy1(request)
        return result
    elif number == 2:
        result = literacy2(request)
        return result
    elif number == 3:
        result = literacy3(request)
        return result
    
def literacy1(request):
    res_data = {}
    if request.method == 'POST':
        if request.POST['answer'] == "  O  ":
            res_data['result'] = "정답입니다."
            user = request.user
            profile = request.user.profile
            profile.score1 = "1"
            profile.save()
        elif request.POST['answer'] == "  X  ":
            res_data['result'] = "다시 한 번 생각해보세요."
    return render(request, 'problem/literacy1.html', res_data)

def literacy2(request):
    res_data = {}
    if request.method == 'POST':
        if request.POST['answer'] == "  O  ":
            res_data['result'] = "정답입니다."
            user = request.user
            profile = request.user.profile
            profile.score2 = "1"
            profile.save()
        elif request.POST['answer'] == "  X  ":
            res_data['result'] = "다시 한 번 생각해보세요."
    return render(request, 'problem/literacy2.html', res_data)

def literacy3(request):
    res_data = {}
    if request.method == 'POST':
        if request.POST['answer'] == "  X  ":
            res_data['result'] = "정답입니다."
            user = request.user
            profile = request.user.profile
            profile.score3 = "1"
            profile.save()
        elif request.POST['answer'] == "  O  ":
            res_data['result'] = "다시 한 번 생각해보세요."
    return render(request, 'problem/literacy3.html', res_data)

# ------------------------------------------------------------
def community(request, number):
    if number == 1:
        result = community1(request)
        return result
    elif number == 2:
        result = community2(request)
        return result
    elif number == 3:
        result = community3(request)
        return result
    
def community1(request):
    res_data = {}
    if request.method == 'POST':
        if request.POST['option'] == "v1":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v2":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v3":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v4":
            res_data['result'] = "정답입니다."
            user = request.user
            profile = request.user.profile
            profile.score7 = "1"
            profile.save()
    return render(request, 'problem/community1.html', res_data)


def community2(request):
    res_data = {}
    if request.method == 'POST':
        if request.POST['option'] == "v1":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v3":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v4":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v2":
            res_data['result'] = "정답입니다."
            user = request.user
            profile = request.user.profile
            profile.score8 = "1"
            profile.save()
    return render(request, 'problem/community2.html', res_data)


def community3(request):
    res_data = {}
    if request.method == 'POST':
        if request.POST['option'] == "v2":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v3":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v4":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v1":
            res_data['result'] = "정답입니다."
            user = request.user
            profile = request.user.profile
            profile.score9 = "1"
            profile.save()
    return render(request, 'problem/community3.html', res_data)


# ------------------------------------------------------------
def sns(request, number):
    if number == 1:
        result = sns1(request)
        return result
    elif number == 2:
        result = sns2(request)
        return result
    elif number == 3:
        result = sns3(request)
        return result

def sns1(request):
    res_data = {}
    if request.method == 'POST':
        if request.POST['option'] == "v1":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v2":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v4":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v3":
            res_data['result'] = "정답입니다."
            user = request.user
            profile = request.user.profile
            profile.score10 = "1"
            profile.save()
    return render(request, 'problem/sns1.html', res_data)


def sns2(request):
    res_data = {}
    if request.method == 'POST':
        if request.POST['option'] == "v1":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v3":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v4":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v5":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v2":
            res_data['result'] = "정답입니다."
            user = request.user
            profile = request.user.profile
            profile.score11 = "1"
            profile.save()
    return render(request, 'problem/sns2.html', res_data)


def sns3(request):
    res_data = {}
    if request.method == 'POST':
        if request.POST['option'] == "v1":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v2":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v4":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v5":
            res_data['result'] = "다시 한 번 생각해보세요."
        elif request.POST['option'] == "v3":
            res_data['result'] = "정답입니다."
            user = request.user
            profile = request.user.profile
            profile.score12 = "1"
            profile.save()
    return render(request, 'problem/sns3.html', res_data)

