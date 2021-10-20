from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# usercreationform을 받아와서 이를 상속받아 한번에 작성한다.
# 상속받은 form에는 여러가지 id와 pw같은 값들을 받아올 수 있는 form이 정의되어 있다.
class CustomUserCreationForm(UserCreationForm):
    # 메타역시도 상속받아사용
    class Meta(UserCreationForm.Meta):
        model = get_user_model()



