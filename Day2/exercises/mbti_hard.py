def ask_questions(questions):
    """사용자에게 질문을 하고 점수를 계산합니다."""
    scores = {"EI": 0, "SN": 0, "TF": 0, "JP": 0}

    for question in questions:
        print(question["text"])
        while True:
            answer = input("(1: 동의하지 않음, 2: 약간 동의, 3: 중립, 4: 약간 동의, 5: 동의): ")
            if answer.isdigit():
                score = int(answer)
                if 1 <= score <= 5:
                    break
            print("유효한 숫자를 입력하세요 (1-5). 다시 시도하세요.")

        if question["dimension"] == "EI":
            scores["EI"] += score - 3
        elif question["dimension"] == "SN":
            scores["SN"] += score - 3
        elif question["dimension"] == "TF":
            scores["TF"] += score - 3
        elif question["dimension"] == "JP":
            scores["JP"] += score - 3

    return scores

def calculate_mbti(scores):
    """점수를 바탕으로 MBTI 유형을 계산합니다."""
    mbti = ""

    if scores["EI"] > 0:
        mbti += "E"
    else:
        mbti += "I"

    if scores["SN"] > 0:
        mbti += "S"
    else:
        mbti += "N"

    if scores["TF"] > 0:
        mbti += "T"
    else:
        mbti += "F"

    if scores["JP"] > 0:
        mbti += "J"
    else:
        mbti += "P"

    return mbti

def main():
    """MBTI 검사기를 실행합니다."""
    questions = [
        # E/I 질문
        {"text": "다른 사람들과 함께하는 시간을 좋아합니까?", "dimension": "EI"},
        {"text": "혼자만의 시간을 더 편안하게 느끼십니까?", "dimension": "EI"},
        {"text": "사회적 활동이 당신을 활력 있게 만드나요?", "dimension": "EI"},

        # S/N 질문
        {"text": "세부사항보다 큰 그림을 보는 것을 선호합니까?", "dimension": "SN"},
        {"text": "실제적이고 구체적인 정보를 선호합니까?", "dimension": "SN"},
        {"text": "아이디어와 가능성에 더 관심이 있습니까?", "dimension": "SN"},

        # T/F 질문
        {"text": "논리적이고 객관적인 결정을 선호합니까?", "dimension": "TF"},
        {"text": "감정과 관계를 고려한 결정을 선호합니까?", "dimension": "TF"},
        {"text": "갈등 상황에서 공정함이 더 중요합니까?", "dimension": "TF"},

        # J/P 질문
        {"text": "계획적이고 조직적인 것을 선호합니까?", "dimension": "JP"},
        {"text": "마감일을 정확히 지키는 것이 중요합니까?", "dimension": "JP"},
        {"text": "즉흥적인 선택이 더 편안하게 느껴지십니까?", "dimension": "JP"},
    ]

    print("MBTI 검사에 오신 것을 환영합니다!")
    scores = ask_questions(questions)
    result = calculate_mbti(scores)
    print(f"\n당신의 MBTI 유형은 {result}입니다!")

if __name__ == "__main__":
    main()
