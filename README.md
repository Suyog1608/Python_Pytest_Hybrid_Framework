# Python_Pytest_Hybrid_Framework


<h2>🔐 loginPage.py - Page Object Model Explanation</h2>

<p>
This file represents the <strong>Login Page</strong> in a Selenium-based Page Object Model (POM) framework.
It contains all the elements and actions related to the login functionality.
</p>

---

<h3>📦 Imported Modules</h3>

<pre><code>from selenium.webdriver.common.by import By</code></pre>
<p>
This imports the <code>By</code> class, which is used to locate elements on a web page (e.g., By.ID, By.NAME, By.XPATH).
</p>

<pre><code>from utils.commonActions import CommonMethod</code></pre>
<p>
This imports a reusable class <code>CommonMethod</code>, which wraps all common Selenium actions like:
<ul>
  <li>Typing into fields</li>
  <li>Clicking elements</li>
  <li>Checking visibility</li>
</ul>
These methods also add <strong>exception handling</strong> and <strong>explicit waits</strong> using <code>WebDriverWait</code>.
</p>

---

<h3>🧱 Class Declaration and Inheritance</h3>

<pre><code>class LoginPage(CommonMethod):</code></pre>
<p>
This means <code>LoginPage</code> is a subclass of <code>CommonMethod</code>.  
It can now use all common utility methods like <code>setInput()</code>, <code>clickElement()</code>, and <code>checkDisplay()</code> from the parent class.
</p>

<pre><code>def __init__(self, driver):
    super().__init__(driver)</code></pre>
<p>
Constructor: Initializes <code>self.driver</code> and <code>self.wait</code> from the <code>CommonMethod</code> using <code>super()</code>.  
This promotes <strong>code reuse</strong> and <strong>DRY principles</strong>.
</p>

---

<h3>🔍 Element Locators</h3>

<pre><code>username_field = (By.NAME, "user_name")
password_field = (By.NAME, "user_password")
login_button   = (By.NAME, "Login")
logo_image     = (By.XPATH, "//img[@src='include/images/vtiger-crm.gif']")
Error_msg      = (By.XPATH, "//*[contains(text(), 'You must specify a valid username and password')]")</code></pre>

<p>
These are **tuples** storing locator strategies (e.g., By.NAME) and their corresponding values.  
They are used to find elements on the login page.
</p>

---

<h3>🌐 open() Method</h3>

<pre><code>def open(self, url):
    self.driver.get(url)</code></pre>
<p>
Opens the login page URL using the provided <code>url</code> parameter.
</p>

---

<h3>🔐 login() Method</h3>

<pre><code>def login(self, username, password):
    self.setUserId(username)
    self.setUserPass(password)
    self.click_login()</code></pre>
<p>
Combines all login steps into a single method: enter username, password, and click login.
</p>

---

<h3>👤 setUserId() Method</h3>

<pre><code># self.driver.find_element(*self.username_field).clear()
# self.driver.find_element(*self.username_field).send_keys(username)</code></pre>

<p>
❌ These lines directly interact with the driver, which is repetitive and lacks wait/exception handling.
</p>

<pre><code>self.setInput(self.username_field, username)</code></pre>
<p>
✅ Replaced with <code>setInput()</code> from CommonMethod.  
It automatically waits for the element, clears it, and sends the input — with exception handling and retry logic.
</p>

---

<h3>🔒 setUserPass() Method</h3>

<pre><code># self.driver.find_element(*self.password_field).clear()
# self.driver.find_element(*self.password_field).send_keys(password)</code></pre>

<p>
❌ Again, direct WebDriver code removed.
</p>

<pre><code>self.setInput(self.password_field, password)</code></pre>
<p>
✅ Reused common method for setting input with safety and reliability.
</p>

---

<h3>🖱️ click_login() Method</h3>

<pre><code># self.driver.find_element(*self.login_button).click()</code></pre>
<p>❌ Direct interaction with WebDriver removed.</p>

<pre><code>self.clickElement(self.login_button)</code></pre>
<p>
✅ Uses <code>clickElement()</code> method which waits for clickability and handles exceptions.
</p>

---

<h3>❌ verify_errorMssg() Method</h3>

<pre><code># return self.driver.find_element(*self.Error_msg).is_displayed()</code></pre>
<p>❌ Direct check on element visibility removed.</p>

<pre><code>return self.checkDisplay(self.Error_msg)</code></pre>
<p>
✅ Uses <code>checkDisplay()</code> which includes <strong>wait + exception handling</strong>.  
Wrapped in <code>try/except</code> so it returns <code>False</code> if error message is not found.
</p>

---

<h3>✅ verify_Logo() Method</h3>

<pre><code># return self.driver.find_element(*self.logo_image).is_displayed()</code></pre>
<p>❌ Raw visibility check removed.</p>

<pre><code>return self.checkDisplay(self.logo_image)</code></pre>
<p>
✅ Better reliability by using utility method from <code>CommonMethod</code> class.
</p>

---

<h2>🔄 Summary: Why These Changes Were Made</h2>

<ul>
  <li>✅ Promote reusability using <code>CommonMethod</code></li>
  <li>✅ Replace repetitive WebDriver code with methods that include <strong>waits and exception handling</strong></li>
  <li>✅ Make the framework <strong>cleaner, scalable, and more maintainable</strong></li>
  <li>✅ Reduce code duplication</li>
  <li>✅ Improve test reliability and reduce flakiness</li>
</ul>

---

<h2>🧠 How This Helps the Framework</h2>

<ul>
  <li>You can reuse <code>CommonMethod</code> in every page class like <code>HomePage</code>, <code>leadPage</code>, etc.</li>
  <li>Reduces 10+ lines of repeated code in every class.</li>
  <li>Standardizes actions like setting input, clicking, and checking visibility.</li>
</ul>

---

<h2>📌 Final Note</h2>

<p>
This is a clean example of applying the **Page Object Model (POM)** + **DRY Principle** + **Exception Safe Utilities** into a Selenium automation framework.
</p>


<h2>📄 leadPage.py – Lead Page Object (POM) Explained</h2>

<p>
This file implements the <strong>Lead Page</strong> object using the Page Object Model (POM). It represents the screen where a user can create a new lead in the application.  
It extends <code>CommonMethod</code> to reuse click and input actions with built-in waits and exception handling.
</p>

---

<h3>📦 Imported Libraries</h3>

<pre><code>from selenium.webdriver.common.by import By</code></pre>
<p>
This Selenium module is used to specify <strong>how elements are located</strong> (by ID, NAME, XPATH, etc.).  
In this file, all locators are defined using <code>By.NAME</code>.
</p>

<pre><code>from utils.commonActions import CommonMethod</code></pre>
<p>
Imports a custom class containing <strong>reusable actions</strong> like:
<ul>
  <li><code>setInput(locator, value)</code> – sends text after waiting</li>
  <li><code>clickElement(locator)</code> – clicks element after waiting</li>
</ul>
Helps reduce repetition and improves stability of test scripts.
</p>

---

<h3>🏷️ Class Declaration</h3>

<pre><code>class leadPage(CommonMethod):</code></pre>
<p>
Defines the <code>leadPage</code> class and inherits from <code>CommonMethod</code> so we can reuse all methods for interacting with web elements.
</p>

---

<h3>🔧 Constructor</h3>

<pre><code>def __init__(self, driver):
    super().__init__(driver)</code></pre>
<p>
Initializes the WebDriver and also sets up the <code>WebDriverWait</code> from the parent <code>CommonMethod</code> class.
</p>

---

<h3>🔍 Element Locators</h3>

<pre><code>
lastname_input = (By.NAME, "lastname")
company_input  = (By.NAME, "company")
save_button    = (By.NAME, "button")
</code></pre>
<p>
Defines the input fields and button on the lead form using <code>By.NAME</code>. These are passed to Selenium for locating UI elements.
</p>

---

<h3>📝 setLastname()</h3>

<pre><code>def setLastname(self, lname):
    self.setInput(self.lastname_input, lname)</code></pre>
<p>
This method enters a last name into the form field using the reusable <code>setInput()</code> method.  
It ensures the element is present and handles timeout/exception internally.
</p>

---

<h3>🏢 setCompany()</h3>

<pre><code>def setCompany(self, comp):
    self.setInput(self.company_input, comp)</code></pre>
<p>
Fills the company name field in the form. Uses the same <code>setInput()</code> method to ensure stability and avoid duplication.
</p>

---

<h3>💾 click_Save()</h3>

<pre><code>def click_Save(self):
    self.clickElement(self.save_button)</code></pre>
<p>
Clicks the Save button after filling out the form.  
The method <code>clickElement()</code> handles waiting for the button to become clickable.
</p>

---

<h3>🧩 create_lead()</h3>

<pre><code>def create_lead(self, lname, comp):
    self.setLastname(lname)
    self.setCompany(comp)
    self.click_Save()</code></pre>
<p>
This method acts as a <strong>wrapper method</strong> that combines all the steps required to create a lead.  
It allows us to call <code>create_lead()</code> in a test file, making test scripts cleaner and easier to read.
</p>

---

<h2>✅ Why This Class is Useful</h2>

<ul>
  <li>📦 Encapsulates all the actions related to the "Lead" feature</li>
  <li>🔄 Reuses logic from <code>CommonMethod</code>, promoting DRY principle</li>
  <li>🧪 Improves test maintainability and readability</li>
  <li>⚙️ Makes the test scripts like <code>test_leadPage.py</code> much cleaner</li>
</ul>

---

<h2>💡 Example Usage in test_leadPage.py</h2>

<pre><code>
ldp = leadPage(driver)
ldp.create_lead("John", "Acme Inc.")
</code></pre>
<p>
This one line will:
<ol>
  <li>Enter the last name "John"</li>
  <li>Enter company "Acme Inc."</li>
  <li>Click the Save button</li>
</ol>
All with built-in waits and error handling.
</p>

---

<h2>📁 Best Practices Followed</h2>

<ul>
  <li>✅ Page Object Model (POM)</li>
  <li>✅ Reusability via inheritance</li>
  <li>✅ Separation of test logic and UI actions</li>
</ul>

---

<p>
You now have a solid <code>leadPage.py</code> POM class that’s scalable and production-friendly.
</p>


<h2>🏠 homePage.py - Page Object Model Explanation</h2>

<p>
This file represents the <strong>Home Page</strong> of the application in the Selenium-Pytest Hybrid Framework.  
It uses Page Object Model (POM) design, and inherits reusable actions from <code>CommonMethod</code>.
</p>

---

<h3>📦 Imported Modules</h3>

<pre><code>from selenium.webdriver.common.by import By</code></pre>
<p>
This is used to specify how Selenium will locate elements on the page, e.g., by <code>ID</code>, <code>NAME</code>, <code>LINK_TEXT</code>, or <code>XPATH</code>.
</p>

<pre><code>from utils.commonActions import CommonMethod</code></pre>
<p>
This imports a custom utility class containing reusable methods like:
<ul>
  <li><code>setInput()</code></li>
  <li><code>clickElement()</code></li>
  <li><code>checkDisplay()</code></li>
</ul>
All these are wrapped with <strong>waits and exception handling</strong> to make tests more stable.
</p>

---

<h3>🧱 Class Declaration</h3>

<pre><code>class HomePage(CommonMethod):</code></pre>
<p>
<code>HomePage</code> is a subclass of <code>CommonMethod</code>, which means it can directly use methods like <code>clickElement()</code> and <code>checkDisplay()</code> without rewriting the logic.
</p>

---

<h3>🛠️ Constructor</h3>

<pre><code>def __init__(self, driver):
    # self.driver = driver
    super().__init__(driver)</code></pre>

<ul>
  <li>❌ <code>self.driver = driver</code>: This line is commented out because the parent class <code>CommonMethod</code> already handles that.</li>
  <li>✅ <code>super().__init__(driver)</code>: Calls the parent class constructor to initialize <code>driver</code> and set up <code>WebDriverWait</code>.</li>
</ul>

---

<h3>🔍 Element Locators</h3>

<pre><code>
home_link    = (By.LINK_TEXT, "Home")
logout_link  = (By.LINK_TEXT, "Logout")
NewLead_link = (By.LINK_TEXT, "New Lead")
</code></pre>
<p>
These are element locators that represent clickable links on the home page.  
Stored as class variables for easy reference in action methods.
</p>

---

<h3>🏡 verifyHome()</h3>

<pre><code># return self.driver.find_element(*self.home_link).is_displayed()</code></pre>
<p>❌ This raw code directly accesses WebDriver and has no waiting or error handling.</p>

<pre><code>return self.checkDisplay(self.home_link)</code></pre>
<p>
✅ Uses <code>checkDisplay()</code> from <code>CommonMethod</code> — which adds:
<ul>
  <li>Explicit wait (using WebDriverWait)</li>
  <li>Exception handling</li>
</ul>
This checks if the "Home" link is visible after login.
</p>

---

<h3>🚪 verifyLogout()</h3>

<pre><code># return self.driver.find_element(*self.logout_link).is_displayed()</code></pre>
<p>❌ Repetitive direct Selenium call, now avoided.</p>

<pre><code>return self.checkDisplay(self.logout_link)</code></pre>
<p>✅ Clean, reusable way to check logout link visibility.</p>

---

<h3>🔓 click_logout()</h3>

<pre><code># self.driver.find_element(*self.logout_link).click()</code></pre>
<p>❌ Clicks the logout link directly — no wait, no handling.</p>

<pre><code>self.clickElement(self.logout_link)</code></pre>
<p>✅ Uses <code>clickElement()</code> which:
<ul>
  <li>Waits for the element to be clickable</li>
  <li>Handles any exceptions</li>
</ul>


---

<h3>🆕 click_NewLead()</h3>

<pre><code>self.clickElement(self.NewLead_link)</code></pre>
<p>
This method clicks on the "New Lead" button/link after successful login.  
It uses the shared <code>clickElement()</code> method for reliability.
</p>

---

<h2>🔄 Summary of Improvements</h2>

<ul>
  <li>✅ Replaces repetitive Selenium code with reusable actions</li>
  <li>✅ Adds stability through waits and exception handling</li>
  <li>✅ Promotes the Page Object Model (POM) and DRY principle</li>
</ul>

---

<h2>📈 Why This is Useful</h2>

<ul>
  <li>You can call <code>HomePage.verifyHome()</code> after login to validate success</li>
  <li>You can perform logout action from anywhere</li>
  <li>This file is the central place for all home page actions, improving maintainability</li>
</ul>

---

<h2>✅ Final Thoughts</h2>

<p>
This is a great example of applying POM and utilities like <code>CommonMethod</code> in real-world test automation.  
This structure allows your framework to scale with ease and reduces maintenance effort in the long run.
</p>

<h2>🧪 test_loginPage.py – Test Class for Login Functionality</h2>

<p>This file contains test cases for the login functionality using the <strong>pytest framework</strong> and the <strong>Page Object Model (POM)</strong>. It imports and uses the methods from <code>LoginPage</code> and <code>HomePage</code> classes to interact with the UI.</p>

<h3>📁 Imports</h3>
<ul>
  <li><code>pytest</code>: Python testing framework</li>
  <li><code>LoginPage</code>: Page class that encapsulates all login-related actions</li>
  <li><code>HomePage</code>: Page class used to verify successful login</li>
</ul>

<h3>⚙️ Test Class: <code>Test_loginPage</code></h3>
<p>This test class is marked with <code>@pytest.mark.usefixtures("browser")</code>, which automatically injects the WebDriver instance into each test case using the fixture defined in <code>conftest.py</code>. The WebDriver is accessed via <code>self.driver</code>.</p>

<h4>🧪 Test Methods:</h4>
<ul>
  <li>
    <strong><code>test_verifyTitle_TCO1(self)</code></strong><br>
    Verifies that the title of the login page matches the expected value: <code>"vtiger CRM - Commercial Open Source CRM"</code>.
  </li>

  <li>
    <strong><code>test_verifyLogo_TC02(self)</code></strong><br>
    Creates an instance of <code>LoginPage</code> and asserts that the CRM logo is displayed on the login page using the <code>Logo()</code> method.
  </li>

  <li>
    <strong><code>test_verify_invalidLogin_TC03(self)</code></strong><br>
    Attempts to log in with invalid credentials. It then verifies that the error message for invalid login is displayed using the <code>errorMssg()</code> method.
  </li>

  <li>
    <strong><code>test_verify_validLogin_TC04(self)</code></strong><br>
    Attempts a valid login using correct credentials. Then it creates an instance of <code>HomePage</code> and asserts that the user has landed on the homepage using the <code>verifyHome()</code> method.
  </li>
</ul>

<h4>✅ Purpose:</h4>
<p>This file serves as the test suite for login functionality. It validates both positive and negative scenarios by interacting with the login page and home page using the Page Object Model approach. The tests are isolated, readable, and maintainable.</p>

<h4>🔁 Reusability:</h4>
<p>Since the tests use the POM design and a browser fixture, they are reusable across multiple browsers and environments without needing code changes.</p>


<h2>⚙️ conftest.py – Centralized Configuration and Fixtures for the Test Suite</h2>

<p>The <code>conftest.py</code> file is used by <strong>pytest</strong> to define shared configurations, fixtures, and hooks that apply to multiple test files. In this project, it manages browser setup, command-line options, and integrates screenshot capturing into the HTML report on test failure.</p>

<hr>

<h3>📦 Imports</h3>

<pre><code>import pytest</code></pre>
<p>Imports the <strong>pytest</strong> framework to define fixtures and hooks.</p>

<pre><code>import pytest_html.extras</code></pre>
<p>Imports extra tools from <code>pytest-html</code> to embed custom HTML content (e.g., screenshots) into the test report.</p>

<pre><code>from selenium import webdriver
from selenium.webdriver.edge.service import Service</code></pre>
<p>Imports Selenium WebDriver and Edge-specific service class to control the Edge browser.</p>

<pre><code>import os
from datetime import datetime</code></pre>
<p><code>os</code> is used to handle directories and paths, while <code>datetime</code> helps create unique timestamps for screenshot file names.</p>

<hr>

<h3>🛠️ Defining Command-Line Option</h3>

<pre><code>def pytest_addoption(parser):</code></pre>
<p>This is a pytest hook to add custom command-line options. Here, we add support for selecting the browser dynamically when running tests.</p>

<pre><code>    parser.addoption("--browser", action="store", default="edge", help="Type in browser name: chrome or edge")</code></pre>
<p>Adds a <code>--browser</code> option to the pytest command. The default is set to "edge", but you can override it using:
<code>pytest --browser=chrome</code></p>

<hr>

<h3>🌐 Browser Fixture</h3>

<pre><code>@pytest.fixture(scope="function")
def browser(request):</code></pre>
<p>Defines a fixture named <code>browser</code> with <code>function</code> scope, meaning it runs before each test function and tears down after it completes.</p>

<pre><code>    bd = request.config.getoption("--browser")</code></pre>
<p>Reads the <code>--browser</code> command-line option selected by the user.</p>

<pre><code>    if bd == "chrome":
        driver = webdriver.Chrome()</code></pre>
<p>If Chrome is selected, it initializes a Chrome browser instance.</p>

<pre><code>    else:
        service = Service(executable_path="C:\\Users\\hp\\PycharmProjects\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=service)</code></pre>
<p>If Chrome is not selected (or default "edge"), it initializes an Edge browser using the EdgeDriver executable.</p>

<pre><code>    driver.get("http://localhost:100")</code></pre>
<p>Opens the application under test in the browser. You can change this to your target URL.</p>

<pre><code>    request.cls.driver = driver
    request.node.driver = driver</code></pre>
<p>Assigns the driver to both <code>request.cls.driver</code> and <code>request.node.driver</code>. 
<ul>
  <li><strong>cls.driver</strong>: Allows test classes to access WebDriver via <code>self.driver</code></li>
  <li><strong>node.driver</strong>: Makes the driver accessible inside pytest hooks like <code>pytest_runtest_makereport</code> for screenshots</li>
</ul>
</p>

<pre><code>    yield driver</code></pre>
<p>Returns the WebDriver instance to the test method.</p>

<pre><code>    driver.quit()</code></pre>
<p>After the test finishes, the browser is closed properly to free up system resources.</p>

<hr>

<h3>📸 Hook: Capture Screenshot on Failure</h3>

<pre><code>@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):</code></pre>
<p>This is a pytest hook that runs after each test case. It's used to inspect the test result and take a screenshot if the test has failed.</p>

<pre><code>    outcome = yield
    report = outcome.get_result()</code></pre>
<p>Executes the actual test and retrieves the test report object (which contains status like passed/failed).</p>

<pre><code>    if report.when == "call" and report.failed:</code></pre>
<p>This condition ensures that we only take screenshots when the test fails during the execution (not during setup).</p>

<pre><code>        driver = getattr(item, "driver", None)</code></pre>
<p>Retrieves the WebDriver instance attached earlier via <code>request.node.driver</code>. Returns <code>None</code> if not available.</p>

<pre><code>        if driver:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)</code></pre>
<p>If the driver exists, a folder named <code>screenshots</code> is created (if not already present).</p>

<pre><code>            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_file = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
            driver.save_screenshot(screenshot_file)</code></pre>
<p>Creates a unique filename using the current time and saves a screenshot of the failed test page.</p>

<pre><code>            if screenshot_file:
                extra = getattr(report, "extra", [])
                html = (f'&lt;div&gt;&lt;img src="{screenshot_file}" alt="screenshot" style="width:300px;height:200px;" '
                        f'onclick="window.open(this.src)" /&gt;&lt;/div&gt;')
                extra.append(pytest_html.extras.html(html))
                report.extra = extra</code></pre>
<p>If a screenshot was taken, this block embeds it into the HTML report using <code>pytest-html</code>. The image is shown as a thumbnail and opens full-size when clicked.</p>

<hr>

<h3>📋 Hook: Capture pytest-html Plugin</h3>

<pre><code>@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):</code></pre>
<p>This hook runs once when pytest starts. It captures the <code>pytest-html</code> plugin object so it can be used later for embedding HTML content (like screenshots).</p>

<pre><code>    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')</code></pre>
<p>Stores the <code>html</code> plugin instance into a global variable so that other functions (like <code>pytest_runtest_makereport</code>) can access it.</p>

<hr>

<h3>✅ Summary</h3>

<ul>
  <li>Manages browser setup and teardown automatically with the <code>browser</code> fixture.</li>
  <li>Supports dynamic browser selection using <code>--browser</code> flag.</li>
  <li>Captures and embeds screenshots into the HTML report if a test fails.</li>
  <li>Centralizes configuration for easier scaling and test maintenance.</li>
</ul>


<h2>🧪 test_leadPage.py – Lead Creation Test Explained</h2>

<p>
This file contains a functional test to automate the process of creating a new lead in a CRM application. It uses the Page Object Model (POM), Excel-based test data, and configuration-driven credentials.
</p>

---

<h3>📦 Imported Modules</h3>

<pre><code>import pytest</code></pre>
<p>
Used to write and run test cases. Provides functionality like fixtures, markers, and assertions.
</p>

<pre><code>from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.leadPage import leadPage</code></pre>
<p>
These are the Page Object classes for different parts of the application. They encapsulate UI logic for Home, Login, and Lead creation respectively.
</p>

<pre><code>from utils.read_excel import read_excel_as_dict_of_dicts</code></pre>
<p>
Custom utility that reads test data from Excel and returns it as a dictionary of dictionaries, which makes test parameterization easy and clean.
</p>

<pre><code>from utils.read_ini import get_ini_data</code></pre>
<p>
This reads data like URLs, usernames, passwords, etc., from the <code>config.ini</code> file using <code>configparser</code>. Keeps sensitive and environment-specific data externalized.
</p>

---

<h3>📊 Reading Excel Data</h3>

<pre><code>login_data_dict = read_excel_as_dict_of_dicts("TestData/testdata.xlsx", "LoginData")</code></pre>
<p>
Loads the <code>LoginData</code> sheet from the given Excel file.  
Returns data in this format:
<pre>
{
  "test_create_lead_TC05": {
    "lastname": "Smith",
    "company": "Infosys"
  }
}
</pre>
</p>

---

<h3>⚙️ Test Class with Fixture</h3>

<pre><code>@pytest.mark.usefixtures("browser")</code></pre>
<p>
Applies the <code>browser</code> fixture to the entire test class.  
This fixture initializes the WebDriver and opens the base URL defined in <code>conftest.py</code>.
</p>

<pre><code>class Test_leadPage:</code></pre>
<p>
Defines the test class that groups all test cases related to lead creation.
</p>

---

<h3>✅ Test Case: test_create_lead_TC05</h3>

<pre><code>def test_create_lead_TC05(self):</code></pre>
<p>
This test automates the entire flow of logging in, navigating to the lead page, filling in the lead form, and logging out.
</p>

---

<h4>🔽 Step-by-Step Breakdown</h4>

<pre><code>row = login_data_dict["test_create_lead_TC05"]</code></pre>
<p>
Extracts the test data for this test case from the Excel dictionary using the test case name as the key.
</p>

<pre><code>lname = row["lastname"]
comp = row["company"]</code></pre>
<p>
Gets the <code>lastname</code> and <code>company</code> values to use in the lead form.
</p>

---

<h4>🔐 Login to the App</h4>

<pre><code>lp = LoginPage(self.driver)</code></pre>
<p>
Initializes the Login Page object with the current driver.
</p>

<pre><code>lp.login(get_ini_data('AppData', 'username'), get_ini_data('AppData', 'password'))</code></pre>
<p>
Logs into the application using credentials stored in <code>config.ini</code>.  
Keeps sensitive data out of code.
</p>

---

<h4>🏠 Verify Home Page</h4>

<pre><code>hp = HomePage(self.driver)
assert hp.verifyHome() == True</code></pre>
<p>
Checks that the Home page is loaded successfully after login.  
This is a simple sanity check to ensure login worked correctly.
</p>

---

<h4>➕ Click "New Lead"</h4>

<pre><code>hp.click_NewLead()</code></pre>
<p>
Clicks the “New Lead” link to navigate to the lead creation form.
</p>

---

<h4>📝 Create New Lead</h4>

<pre><code>ldp = leadPage(self.driver)
ldp.create_lead(lname, comp)</code></pre>
<p>
Initializes the <code>leadPage</code> object and calls <code>create_lead()</code> to fill out and submit the form using Excel data.
</p>

---

<h4>🚪 Logout</h4>

<pre><code>hp.click_logout()</code></pre>
<p>
Logs the user out of the application.  
This ensures the session ends properly and sets up a clean state for future tests.
</p>

---

<h2>🧠 Key Concepts in This Test</h2>

<ul>
  <li>✅ POM used for code reusability and readability</li>
  <li>📊 Excel data-driven testing implemented via <code>read_excel_as_dict_of_dicts()</code></li>
  <li>🔐 Config data like username/password handled via <code>read_ini.py</code></li>
  <li>💡 Clean and scalable test automation design</li>
</ul>

---

<h2>📁 Related Files That Make This Work</h2>

<ul>
  <li><strong>Pages/leadPage.py</strong> – Logic to fill and submit lead form</li>
  <li><strong>utils/read_excel.py</strong> – Excel reader as dictionary</li>
  <li><strong>utils/read_ini.py</strong> – Reads config values</li>
  <li><strong>conftest.py</strong> – Manages driver and fixtures</li>
</ul>

---

<h2>🔁 Sample testdata.xlsx Format</h2>

<table>
  <thead>
    <tr>
      <th>TCName</th>
      <th>lastname</th>
      <th>company</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>test_create_lead_TC05</td>
      <td>Smith</td>
      <td>Infosys</td>
    </tr>
  </tbody>
</table>

---

<p>
This test file is a complete example of how to combine <strong>POM + Excel + Config + Pytest fixtures</strong> for scalable test automation.
</p>


<h2>💻 Commands to Run Test Cases</h2>

<p>This section provides all the commands you can use to run the Selenium-Pytest test cases in this framework.</p>

<hr>

<h3>1️⃣ Run All Test Cases in the Project</h3>
<pre><code>pytest</code></pre>
<p>Runs all test cases in the current directory and subdirectories using the default browser specified in <code>conftest.py</code>.</p>

<hr>

<h3>2️⃣ Run a Specific Test File</h3>
<pre><code>pytest TestCases/test_loginPage.py</code></pre>
<p>Runs all test cases inside <code>test_loginPage.py</code>.</p>

<hr>

<h3>3️⃣ Run a Single Test Case</h3>
<pre><code>pytest TestCases/test_loginPage.py::Test_loginPage::test_verifyTitle_TCO1</code></pre>
<p>Runs only the test method <code>test_verifyTitle_TCO1</code> from <code>Test_loginPage</code> class.</p>

<hr>

<h3>4️⃣ Run Tests in a Specific Browser</h3>
<pre><code>pytest --browser=chrome
pytest --browser=edge</code></pre>
<p>Selects the browser dynamically at runtime using the <code>--browser</code> option defined in <code>conftest.py</code>.</p>

<hr>

<h3>5️⃣ Use <code>-s</code> and <code>-v</code> Options</h3>
<ul>
  <li><code>-s</code>: Allows printing <code>print()</code> statements to the console.</li>
  <li><code>-v</code>: Verbose mode – shows detailed test results including test names and statuses.</li>
</ul>

<pre><code>pytest -s -v
pytest -s -v TestCases/test_loginPage.py
pytest -s -v TestCases/test_loginPage.py::Test_loginPage::test_verifyTitle_TCO1</code></pre>

<hr>

<h3>6️⃣ Generate HTML Report</h3>
<pre><code>pytest --browser=edge --html=reports/report.html --self-contained-html</code></pre>
<p>Generates an HTML report in the <code>reports</code> folder. <code>--self-contained-html</code> embeds all resources (like screenshots) into a single file.</p>

<hr>

<h3>7️⃣ Run Tests and Capture Screenshots on Failure</h3>
<p>With the <code>conftest.py</code> hook configured, any failed test automatically captures a screenshot in the <code>screenshots</code> folder and embeds it into the HTML report.</p>

<pre><code>pytest --browser=edge --html=reports/report.html --self-contained-html -v -s</code></pre>

<hr>

<h3>8️⃣ Run Tests in Parallel (using pytest-xdist)</h3>
<pre><code>pytest -n 2</code></pre>
<p>Runs tests in parallel using 2 CPU cores. You can increase the number (<code>-n 4</code>, etc.) based on your machine capacity.</p>

<pre><code>pytest -n 2 --browser=chrome --html=reports/report.html --self-contained-html</code></pre>
<p>Runs all tests in parallel, on Chrome, with HTML report and screenshots on failure.</p>

<hr>

<h3>9️⃣ Additional Useful Options</h3>
<ul>
  <li><code>--maxfail=1</code>: Stops test execution after 1 failure.</li>
  <li><code>--tb=short</code>: Shows a shorter traceback in the console.</li>
  <li><code>--disable-warnings</code>: Hides warnings in the console output.</li>
</ul>

<pre><code>pytest -v -s --maxfail=1 --tb=short --disable-warnings</code></pre>

<hr>

<h3>📌 Notes:</h3>
<ul>
  <li>Make sure your <code>screenshots</code> and <code>reports</code> folders exist or they will be created automatically by the framework.</li>
  <li>Always use the <code>--browser</code> flag to control which browser to run tests on.</li>
  <li>Combine <code>-s</code>, <code>-v</code>, <code>-n</code>, and <code>--html</code> options as needed for debugging, reporting, or parallel execution.</li>
</ul>


<h2>📄 read_ini.py - Configuration File Reader</h2>

<p>
The <code>read_ini.py</code> file is used to read application configuration data (like URLs, usernames, passwords, locator paths, etc.) from an external <code>config.ini</code> file using Python's built-in <code>configparser</code> module.
This allows you to separate hardcoded data from test logic, making your framework more <strong>flexible, maintainable, and reusable</strong>.
</p>

<pre><code>import configparser</code></pre>
<p><strong>Why?</strong> This is a built-in Python module that provides a way to handle configuration files like <code>.ini</code>. It lets you read sections and keys from the file as if they were dictionaries.</p>

<pre><code>import os</code></pre>
<p><strong>Why?</strong> The <code>os</code> module is used to handle file paths dynamically, so the code works on any system (Windows, Mac, Linux). It ensures we can locate <code>config.ini</code> reliably, regardless of the current working directory.</p>

<pre><code>base_dir = os.path.dirname(os.path.abspath(__file__))</code></pre>
<p>This line finds the absolute directory path of the current file (<code>read_ini.py</code>). It ensures that even if the test is run from a different location, the script can still find the config file correctly.</p>

<pre><code>config_path = os.path.join(base_dir, 'config.ini')</code></pre>
<p>This combines the base path with the <code>config.ini</code> filename. Now we have the full path to the configuration file.</p>

<pre><code>print(f"Trying to read config file at: {config_path}")</code></pre>
<p>Simple debug statement to confirm where it is looking for the config file.</p>

<pre><code>config = configparser.ConfigParser()</code></pre>
<p>This creates a <code>ConfigParser</code> object to start reading from the config file.</p>

<pre><code>files_read = config.read(config_path)</code></pre>
<p>This reads the <code>config.ini</code> file from the path we built. It returns a list of successfully read files.</p>

<pre><code>print(f"Config files loaded: {files_read}")</code></pre>
<p>Prints which files were loaded (for debugging).</p>

<pre><code>print(f"Sections found: {config.sections()}")</code></pre>
<p>Lists all the section names found in the <code>config.ini</code> file (e.g., <code>[AppData]</code>, <code>[locators]</code>).</p>

<pre><code>def get_ini_data(block, key):</code></pre>
<p>This function helps retrieve values from the config file. For example, it can return the URL, username, or a locator by giving section name and key.</p>

<pre><code>    try:
        return config[block][key]
    except KeyError as e:
        raise KeyError(f"Missing section/key: {e}")</code></pre>
<p>This tries to fetch the value and raises a readable error if the section or key is not found.</p>

<pre><code>print(get_ini_data('AppData', 'url'))</code></pre>
<p>This line is just a test to show the value retrieved from <code>[AppData]</code> section, for the key <code>url</code>.</p>

---

<h2>📁 config.ini - Example Structure</h2>

<pre><code>[AppData]
url = http://localhost:100
username = admin
password = admin

[locators]
login_button = //button[@id="login"]</code></pre>

---

<h2>🔗 How it's used in <code>commonActions.py</code></h2>

<p>You can use <code>get_ini_data()</code> inside any class like <code>CommonMethod</code> to avoid hardcoding locators, URLs, and credentials. Example:</p>

<pre><code>from utils.read_ini import get_ini_data

url = get_ini_data("AppData", "url")
username = get_ini_data("AppData", "username")
</code></pre>

<p>This helps in:</p>
<ul>
  <li>🔄 Updating URLs or credentials without touching code</li>
  <li>📄 Storing environment-specific data cleanly</li>
  <li>🧪 Running the same tests against different environments (QA, staging, prod)</li>
</ul>

---

<h2>🎯 Why this is important?</h2>
<p>This approach follows the principle of <strong>Separation of Concerns</strong>. Instead of hardcoding values in test scripts or page objects, we externalize them, making our framework:</p>

<ul>
  <li>✅ More maintainable</li>
  <li>🔧 Easily configurable</li>
  <li>🧩 Scalable for different environments or user types</li>
</ul>

---

<h2>✅ Summary</h2>

<ul>
  <li><code>configparser</code> reads values from <code>.ini</code> files</li>
  <li><code>get_ini_data()</code> is a helper to fetch any config value</li>
  <li>Used across your framework in <code>loginPage</code>, <code>homePage</code>, <code>commonActions</code>, etc.</li>
  <li>Avoids hardcoding, supports easy config changes</li>
</ul>


<h2>📄 commonActions.py - HTML Explanation</h2>

<p>
The <code>commonActions.py</code> file defines a helper class <strong>CommonMethod</strong> which contains reusable utility methods for interacting with web elements using Selenium. This helps avoid code duplication and centralizes common interactions like setting input fields, clicking buttons, and verifying element visibility.
</p>

---

<h3>🔍 Imported Libraries & Why They're Used</h3>

<pre><code>from selenium.webdriver.support import expected_conditions as EC</code></pre>
<p>
✅ <code>expected_conditions</code> (imported as <code>EC</code>) provides a collection of pre-built conditions you can wait for — like an element becoming clickable, visible, or present in the DOM.  
It is used with WebDriverWait to perform **explicit waits**.
</p>

<pre><code>from selenium.common import NoSuchElementException, TimeoutException</code></pre>
<p>
✅ These are built-in Selenium exceptions:
<ul>
  <li><code>NoSuchElementException</code>: Raised when the element could not be found in the DOM.</li>
  <li><code>TimeoutException</code>: Raised when an explicit wait times out (element doesn’t appear or isn't ready in the given time).</li>
</ul>
</p>

<pre><code>from selenium.webdriver.support.wait import WebDriverWait</code></pre>
<p>
✅ <code>WebDriverWait</code> is used for explicit waits. You tell Selenium to "wait up to X seconds until a condition is met". This helps deal with dynamic content where elements load slowly.
</p>

---

<h3>🚀 Class: CommonMethod</h3>

<pre><code>class CommonMethod:</code></pre>
<p>This defines a reusable class for commonly used web actions like input, click, and display checks.</p>

---

<h4>🔧 Constructor</h4>

<pre><code>def __init__(self, driver):</code></pre>
<p>
Constructor method that accepts a Selenium <code>driver</code> object so that the class can interact with the browser.
</p>

<pre><code>self.driver = driver</code></pre>
<p>Saves the driver instance for reuse in class methods.</p>

<pre><code>self.wait = WebDriverWait(driver, 10)</code></pre>
<p>
Sets up a default explicit wait of 10 seconds. This will be used to wait for elements to load or become clickable.
</p>

---

<h3>📝 Method: setInput()</h3>

<pre><code>def setInput(self, locator, value):</code></pre>
<p>Used to enter text into input fields.</p>

<pre><code>element = self.wait.until(EC.presence_of_element_located(locator))</code></pre>
<p>
✅ Waits until the element (using the <code>locator</code>) is present in the DOM. Prevents errors due to timing issues.
</p>

<pre><code>element.clear()</code></pre>
<p>Clears any existing text in the input field before sending new text.</p>

<pre><code>element.send_keys(value)</code></pre>
<p>Types the given value into the input field.</p>

<pre><code>except TimeoutException:</code></pre>
<p>❌ If the element isn’t found within 10 seconds, catch this exception and show a readable error.</p>

<pre><code>print(f"Timeout: Element not found for input: {locator}")</code></pre>
<p>Logs the issue for debugging purposes.</p>

<pre><code>raise</code></pre>
<p>Re-throws the caught exception so that test fails and full traceback is preserved in reports.</p>

<pre><code>except NoSuchElementException:</code></pre>
<p>❌ If the element doesn't exist at all in the DOM, catch this and raise again with logging.</p>

---

<h3>🖱️ Method: clickElement()</h3>

<pre><code>def clickElement(self, locator):</code></pre>
<p>This method is used to perform a click action on the given element.</p>

<pre><code>element = self.wait.until(EC.presence_of_element_located(locator))</code></pre>
<p>Waits until the element is available in the DOM.</p>

<pre><code>element.click()</code></pre>
<p>Clicks the element once it becomes available.</p>

<pre><code>except TimeoutException:</code></pre>
<p>If the element never appears in 10 seconds, logs the timeout issue and re-raises the exception.</p>

<pre><code>except NoSuchElementException:</code></pre>
<p>Handles cases where element is not found at all.</p>

---

<h3>👀 Method: checkDisplay()</h3>

<pre><code>def checkDisplay(self, locator):</code></pre>
<p>
Returns <code>True</code> if the element is displayed on the screen.
</p>

<pre><code>element = self.wait.until(EC.presence_of_element_located(locator))</code></pre>
<p>Waits for the element to appear in the DOM.</p>

<pre><code>return element.is_displayed()</code></pre>
<p>
Checks and returns if the element is visible on the UI. This is useful for validations.
</p>

<pre><code>except Exception:</code></pre>
<p>
Catches <strong>any kind of error</strong> (not just Timeout or NoSuchElement) and logs it. This is a catch-all error handler.
</p>

<pre><code>raise</code></pre>
<p>Re-throws the error to make the test fail and report the issue.</p>

---

<h3>🔑 Why is <code>locator</code> passed in all functions?</h3>
<p>
A <code>locator</code> is a tuple like <code>(By.XPATH, "//input[@id='username']")</code>.  
By passing it as a parameter, we make the methods reusable for any page, any element.
</p>

---

<h3>🎯 Summary</h3>

<ul>
  <li>✅ <code>setInput()</code> - Types into input fields</li>
  <li>✅ <code>clickElement()</code> - Clicks buttons/links</li>
  <li>✅ <code>checkDisplay()</code> - Validates if element is visible</li>
  <li>📦 Uses <code>WebDriverWait</code> for stable element interaction</li>
  <li>⚠️ Uses <code>try-except-raise</code> pattern for clear error handling and test failure</li>
  <li>🧩 You can call this from any page object (e.g., LoginPage, HomePage) to reduce code duplication</li>
</ul>

---

<h3>📌 Example Usage in Page Object</h3>

<pre><code>from utils.commonActions import CommonMethod

class LoginPage:
    username_field = (By.NAME, "user_name")

    def __init__(self, driver):
        self.driver = driver
        self.action = CommonMethod(driver)

    def login(self, username):
        self.action.setInput(self.username_field, username)
</code></pre>
<p>This makes your code cleaner, shorter, and more maintainable.</p>


<h2>📄 read_excel.py - HTML Explanation</h2>

<p>
The function <code>read_excel_as_dict_of_dicts</code> is used to read test data from an Excel file and convert it into a dictionary of dictionaries.  
This allows for flexible, readable, and dynamic data-driven testing in your framework.
</p>

---

<h3>📦 Imported Library</h3>

<pre><code>from openpyxl import load_workbook</code></pre>
<p>
✅ <code>openpyxl</code> is a Python library used to read/write Excel 2010 files (i.e., .xlsx).  
Here, we import <code>load_workbook</code>, which loads the Excel file into memory so we can work with it.
</p>

---

<h3>🧠 Function Definition</h3>

<pre><code>def read_excel_as_dict_of_dicts(file_path, sheet_name, key_column="TCName"):</code></pre>
<p>
Defines a function that:
<ul>
  <li><strong>file_path</strong>: path to the Excel file (e.g., "TestData/testdata.xlsx")</li>
  <li><strong>sheet_name</strong>: the name of the Excel sheet to read (e.g., "LoginData")</li>
  <li><strong>key_column</strong>: the name of the column whose values will become the keys in the outer dictionary (default is "TCName")</li>
</ul>
</p>

---

<h3>📂 Load Excel Sheet</h3>

<pre><code>workbook = load_workbook(file_path)</code></pre>
<p>Loads the Excel workbook (.xlsx file) from the given file path.</p>

<pre><code>sheet = workbook[sheet_name]</code></pre>
<p>Accesses the specific sheet (like "LoginData" or "LeadData") from the workbook.</p>

---

<h3>📝 Extract Header Row</h3>

<pre><code>headers = [cell.value for cell in sheet[1]]</code></pre>
<p>
Takes the first row (sheet[1]) which usually contains column titles (e.g., TCName, username, password) and stores them in a list called <code>headers</code>.
</p>

<pre><code>key_index = headers.index(key_column)</code></pre>
<p>
Finds the index of the column you want to use as the <strong>main dictionary key</strong> (e.g., "TCName" column).
</p>

---

<h3>📊 Initialize the Final Data Dictionary</h3>

<pre><code>data = {}</code></pre>
<p>Creates an empty dictionary to hold all the test data, keyed by test case name.</p>

---

<h3>🔁 Loop Through the Excel Rows</h3>

<pre><code>for row in sheet.iter_rows(min_row=2, values_only=True):</code></pre>
<p>
Loops through each row in the sheet starting from the second row (to skip headers).  
<code>values_only=True</code> returns a tuple of cell values for each row.
</p>

<pre><code>key = row[key_index]</code></pre>
<p>Fetches the value of the cell in the key column — this will become the dictionary key (e.g., "test_create_lead_TC05").</p>

<pre><code>row_dict = {headers[i]: row[i] for i in range(len(headers)) if i != key_index}</code></pre>
<p>
Builds a dictionary of the current row’s data using headers as keys, but skips the key column itself (since it’s already used as the outer key).
</p>

<pre><code>data[key] = row_dict</code></pre>
<p>Adds the row's dictionary to the main data dictionary with the test case name as the key.</p>

---

<h3>📤 Return the Final Dictionary</h3>

<pre><code>return data</code></pre>
<p>Returns a dictionary of dictionaries containing all test data, like this:</p>

<pre><code>
{
  "test_create_lead_TC05": {
    "lastname": "Smith",
    "company": "Infosys"
  },
  "test_invalid_login_TC03": {
    "username": "invalid",
    "password": "1234"
  }
}
</code></pre>

---

<h3>📌 Example Excel File (testdata.xlsx)</h3>

| TCName                | username | password | lastname | company |
|----------------------|----------|----------|----------|---------|
| test_valid_login_TC01 | admin    | admin    |          |         |
| test_create_lead_TC05 |          |          | Smith    | Infosys |

---

<h3>✅ How This Function Is Used</h3>

<pre><code>from utils.read_excel import read_excel_as_dict_of_dicts

login_data_dict = read_excel_as_dict_of_dicts("TestData/testdata.xlsx", "LoginData")

row = login_data_dict["test_create_lead_TC05"]
lname = row["lastname"]
comp = row["company"]
</code></pre>

<p>
This allows you to:
<ul>
  <li>Keep test data separate from test logic</li>
  <li>Easily update test data without touching your Python files</li>
  <li>Use data-driven testing for multiple test scenarios</li>
</ul>

