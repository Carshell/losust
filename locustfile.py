import asyncio
import time
from locust import User, task, between
from playwright.async_api import async_playwright
import random 
import string

def generate_random_user():

    first_name = ''.join(random.choices(string.ascii_lowercase, k=6)).capitalize()
    last_name = ''.join(random.choices(string.ascii_lowercase, k=8)).capitalize()
    
    random_numbers = random.randint(100, 999)
    email = f"{first_name.lower()}{last_name.lower()}{random_numbers}@gmail.com"
    
    random_digits = ''.join(random.choices(string.digits, k=9))
    phone = f"+380{random_digits}"
    
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(password_characters, k=10))
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "password": password
    }

class PlaywrightUser(User):
    wait_time = between(1, 3)

    def on_start(self):
        self.loop = asyncio.new_event_loop()

    async def _run_playwright_task(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            start_time = time.perf_counter()
            user = generate_random_user()
            try:
                await page.goto("https://akcenter.com.ua/")
                await page.get_by_text("кабінет").click()
                await page.wait_for_timeout(2000)
                await page.get_by_text("Реєстрація").click()
                await page.wait_for_timeout(2000)
                await page.locator("#input-firstname").fill(user["first_name"])
                await page.locator("#input-lastname").fill(user["last_name"])
                await page.locator("#input-email").fill(user["email"])
                await page.locator("#input-telephone").fill(user["phone"])
                await page.locator("#input-password").fill(user["password"])
                await page.locator("#input-confirm").fill(user["password"])
                await page.wait_for_timeout(2000)
                await page.get_by_text("Продовжити").click()
                await page.wait_for_timeout(2000)
                await page.goto("https://akcenter.com.ua/kanctovari/atlasi-karti-hlobusy")
                await page.wait_for_timeout(2000)
                await page.mouse.wheel(0, 800)

                total_time = int((time.perf_counter() - start_time) * 1000)
                self.environment.events.request.fire(
                    request_type="playwright",
                    name="example_page",
                    response_time=total_time,
                    response_length=0,
                    exception=None,
                )
            except Exception as e:
                total_time = int((time.perf_counter() - start_time) * 1000)
                self.environment.events.request.fire(
                    request_type="playwright",
                    name="example_page",
                    response_time=total_time,
                    response_length=0,
                    exception=e,
                )
            finally:
                #await browser.close()
                pass

    @task
    def playwright_task(self):
        self.loop.run_until_complete(self._run_playwright_task())
