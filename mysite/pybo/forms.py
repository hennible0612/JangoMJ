from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm): #QuestionForm 은 forms.odelForm을 상속했다.
    """
    장고는 일반 폼 forms.Form 과 모델폼 forms.ModelForm이 있는데 모델 폼은 모델과 연결된 폼으로 폼을 저장함녀 연결된 모델의 데이터를 저장할수 있는 폼이댜.
    """
    class Meta: #모델폼은 이너 클래스인 Meta 클래스가 반드시 필요하다. Meta 클래스에는 사용할 모델과 모데르이 속성을 적어야한다.
        """
        즉,QuestionForm은 Question 모델과 연결되 폼이고 속성으로 Question모델의 subject와 content를 사용한다고 정의한 것이다.
        """
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성


        #{{ form.as_p }} 태그는 html코드를 자동으로 생성하ㅣㄱ 때문에 부트스트랩을 적용할 수가 없다.
        #하지만 아래 처럼 수정하면 어느정도 해결이 가능하다.
        # model = Question
        # fields = ['subject', 'content']
        # widgets ={
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control','rows':10}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }