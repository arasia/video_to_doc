def get_prompt(full_transcript):
    return f"""
            아래의 내용은 전문 소프트웨어 엔지니어가 자신의 기술적 지식을 나누는 대화의 녹음본입니다.  
            이 내용을 기반으로 기술 문서를 작성해 주세요.

            작성 시 반드시 다음 지침을 준수하세요:  
            - 문서 작성 언어: 한국어로 작성합니다.  
            - 문서의 형식: Markdown 형태로 작성합니다.  
                - 제목, 부제목, 목록, 코드 블록 등을 적절히 사용하여 문서를 구조화하세요.  
            - 문체 및 품격: 기술 문서의 형식을 따르며, 다음을 준수하세요:  
                - 대화체, 감정 표현, 유머 등은 배제하고 문어체를 사용합니다.  
                - 기술적 내용만 포함하며, 녹음 내용에 없는 정보를 추가하지 않습니다.  
                - 부록이 필요하다면 추가로 작성하세요.
                - 신뢰 가능한 문서가 되도록 노력하세요.
            - 문서 제목: 녹음 내용의 핵심 키워드로 제목을 선정합니다.  
            - 문서 구조: 다음 구조를 따르세요:  
                1. 제목: 핵심 주제를 명확히 표현.  
                2. 개요: 다룰 내용의 요약.  
                3. 본문: 주요 개념, 원리, 사용 방법 등을 상세히 설명.
                4. 결론 (선택 사항): 주요 요점 정리 및 참고 자료 제공.
            - 기타 사항:
                - 이것이 녹음본이라고 이야기 하지 마세요
                - 본문에 인용 번호, 참고 번호를 부여하지 마세요

            ```
            {full_transcript}
            ```
            """
