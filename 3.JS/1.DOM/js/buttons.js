    function number_inc({
            let number = document.getElementById('result');
            let number_string = number.textContent;
            // div 요소 안에 있는 긍르 가져오는 3가지 방식
            // innerText- 글자만 가져오기 (디자인 속성 적용)
            // innerHTML - 글자와 태그까지 함께 가져외
            // textContent - 순수글자만 가져오기

            let number_string_t_number = Number(number_string)
            let result =  number_string_t_number + 1;
            number.textContent = result ;


        })

    function number_dec({
            let result = document.getElementById('result');
            result.textContent = Number(result.textContent ) - 1 ;
        })