'''Модульные тесты'''
'''Тестируем стэк'''

'''
stack = []  # В питоне стек реализован через список
not stack  # Список пуст
# True
stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
not stack  # Список не пустой
# False
stack
# [1, 2, 3]
stack.pop()  # В стеке [1, 2]
# 3
stack.pop()  # В стеке [1]
# 2
stack.pop()  # В стеке пусто
# 1
not stack
# True
'''

# Тестируем основную функциональность
def test_stack():
    stack = []
    # Добавляем два элемента в стек и затем извлекаем их
    # Почему два? Так надежнее, чем один, а три скорее всего избыточно
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


# Тестируем дополнительную функциональность
def test_emptiness():
    # проверка на пустоту
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack


# Пограничные случаи
#import pytest

def test_pop_with_empty_stack():
    # извлечь элемент, когда в стеке нет ни одного элемента
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
