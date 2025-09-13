# Python_Pytest_Hybrid_Framework


<h2>📄 loginPage.py – Page Object Model for Login Functionality</h2>

<p>This file represents the Page Object Model (POM) for the Login Page of the application under test. It contains all the locators and methods related to interacting with the login page using Selenium WebDriver.</p>

<h3>🔧 Class: <code>LoginPage</code></h3>

<p>The <code>LoginPage</code> class is initialized with a WebDriver instance and provides encapsulated methods to perform actions like entering username, password, clicking the login button, and verifying UI elements like logo or error messages.</p>

<h4>🔑 Locators (Defined as Class Variables)</h4>
<ul>
  <li><code>username_field</code>: Locates the username input field by name (<code>user_name</code>).</li>
  <li><code>password_field</code>: Locates the password input field by name (<code>user_password</code>).</li>
  <li><code>login_button</code>: Locates the login button by name (<code>Login</code>).</li>
  <li><code>logo_image</code>: Locates the CRM logo image using XPath.</li>
  <li><code>Error_msg</code>: Locates the error message for invalid login using XPath and partial text match.</li>
</ul>

<h4>🛠 Methods:</h4>

<ul>
  <li>
    <code>__init__(self, driver)</code>: Constructor method to initialize the WebDriver instance for the class.
  </li>
  <li>
    <code>open(self, url)</code>: Opens the given URL using the WebDriver.
  </li>
  <li>
    <code>login(self, username, password)</code>: Wrapper method that calls <code>setUserId</code>, <code>setUserPass</code>, and <code>click_login</code> to perform a login.
  </li>
  <li>
    <code>setUserId(self, username)</code>: Clears and fills the username field.
  </li>
  <li>
    <code>setUserPass(self, password)</code>: Clears and fills the password field.
  </li>
  <li>
    <code>click_login(self)</code>: Clicks the login button.
  </li>
  <li>
    <code>errorMssg(self)</code>: Checks if the invalid login error message is displayed and returns a boolean.
  </li>
  <li>
    <code>Logo(self)</code>: Verifies whether the CRM logo is displayed and returns a boolean.
  </li>
</ul>

<h4>✅ Purpose:</h4>
<p>This class follows the Page Object Model (POM) design pattern to keep UI locators and test logic separate. It promotes reusability, maintainability, and better readability of the test framework.</p>



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



<h2>📄 homePage.py – Page Object Model for Home Page</h2>

<p>This file represents the Page Object Model (POM) for the Home Page of the application. It contains all locators and methods related to interacting with the Home Page using Selenium WebDriver.</p>

<h3>🔧 Class: <code>HomePage</code></h3>

<p>The <code>HomePage</code> class is initialized with a WebDriver instance and provides methods to verify the visibility of homepage elements and perform actions like logout.</p>

<h4>🔑 Locators (Defined as Class Variables)</h4>
<ul>
  <li><code>home_link</code>: Locates the "Home" link on the page using <code>By.LINK_TEXT</code>.</li>
  <li><code>logout_link</code>: Locates the "Logout" link on the page using <code>By.LINK_TEXT</code>.</li>
</ul>

<h4>🛠 Methods:</h4>
<ul>
  <li>
    <code>__init__(self, driver)</code>: Constructor method to initialize the WebDriver instance for the class.
  </li>
  <li>
    <code>verifyHome(self)</code>: Checks if the "Home" link is displayed on the page. Returns <code>True</code> if visible, <code>False</code> otherwise.
  </li>
  <li>
    <code>verifyLogout(self)</code>: Checks if the "Logout" link is displayed on the page. Returns <code>True</code> if visible, <code>False</code> otherwise.
  </li>
  <li>
    <code>click_logout(self)</code>: Clicks the "Logout" link to log out from the application.
  </li>
</ul>

<h4>✅ Purpose:</h4>
<p>This class follows the Page Object Model (POM) design pattern to encapsulate home page interactions. It keeps locators and test logic separate, which improves reusability, maintainability, and readability in the test framework.</p>

<h4>🔁 Reusability:</h4>
<p>The methods in <code>HomePage</code> can be reused in multiple test cases wherever home page interactions are required, like verifying successful login or logging out.</p>



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
