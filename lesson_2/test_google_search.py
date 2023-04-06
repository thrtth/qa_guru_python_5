import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def open_browser():
    browser.open('https://google.com')
    browser.driver.set_window_size(1500, 800)
    yield
    browser.close()

# @pytest.fixture
# def close_browser():
#     yield
#     browser.close()


def test_search_selene(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_nonexistent(open_browser):
    browser.element('[name="q"]').should(be.blank).type('jahsdguywrtwegajhsdgfuye').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
