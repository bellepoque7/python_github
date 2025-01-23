# import sys
# print(sys.version)
import seaborn as sns

def get_tips():
    tips = sns.load_dataset('tips')
    return tips


def print_get():
    return '일어나세요 용사여'


if __name__ == '__main__':
    print('''
    1. get_tips: tips 데이터 로드
    2. print_get "일어나세요 용사여" 출력
    ''')
    choice = input()
    if choice == '1':
        print('tips 로드가 완료되었습니다.')
        get_tips()
    elif choice == '2':
        print('print_get 함수가 실행되었습니다.')
        print_get()