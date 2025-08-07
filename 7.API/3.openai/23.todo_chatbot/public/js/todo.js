console.log('todo.js 실행')

const todoForm = document.getElementById('todo-form')
const textInput = document.getElementById('text-input')
const todoList = document.getElementById('todo-list')

document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('/api/todo');
    const todos = await response.json();
    todos.forEach(renderTodo);
})

function renderTodo(todo) {
    const li = document.createElement('li');
    li.textContent = todo.text;
    if (todo.completed) {
        li.style.textDecoration = 'line-through';
    };

    // innerHTML -> 보안상 좋지 않다 -> 입력값 검증하기
    // li.innerHTML = `
    //     <span class="${todo.completed ? 'line-through':'none'}">
    //         ${todo.text}
    //     </span>
    //     <a><i class="bi bi-trash"></i></ a>
    //     `;
    // todoList.appendChild(li);
    
    li.addEventListener('click', async () => {
        const response = await fetch(`/api/todo/${todo.id}`, {
            method: 'PUT'
        });
        const update = await response.json();
        li.style.textDecoration = update.completed ? 'line-through': 'none';
    });

    const delBtn = document.createElement('button');
    delBtn.innerHTML = '<i class="bi bi-trash"></i>';
    delBtn.addEventListener('click', async (e) => {
        e.stopPropagation();
        await fetch(`/api/todo/${todo.id}`, {
            method: 'DELETE'
        });
        li.remove();
    });
    li.appendChild(delBtn);

    todoList.appendChild(li);
}

todoForm.addEventListener('submit', submitForm)

async function submitForm(e) {
    e.preventDefault();
    const text = textInput.value.trim();
    if (!text) return;

    let response;

    try {
        response = await fetch('/api/todo', { 
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body:  JSON.stringify({text: text})
        })
    } catch (err) {
        console.error('백엔드 요청에 실패하였습니다: ', err);
    }

    textInput.value = '';
    
    const newTodo = await response.json();
    renderTodo(newTodo);
}

