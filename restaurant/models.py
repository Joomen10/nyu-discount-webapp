<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <style>
        /* General Styles */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            width: 350px;
            text-align: center;
        }

        h2 {
            color: #333;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
            text-align: left;
        }

        label {
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }

        .email-group {
            display: flex;
            align-items: center;
        }

        .email-group input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px 0 0 5px;
            font-size: 14px;
            outline: none;
        }

        .email-group span {
            background-color: #ddd;
            padding: 10px;
            border: 1px solid #ccc;
            border-left: none;
            border-radius: 0 5px 5px 0;
            font-size: 14px;
            color: #555;
            white-space: nowrap;
        }

        input, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 14px;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #007bff;
            box-shadow: 0px 0px 5px rgba(0, 123, 255, 0.5);
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
            transition: 0.3s;
        }

        button:hover {
            background-color: #0056b3;
        }

        #response-message {
            margin-top: 15px;
            font-size: 14px;
            color: #28a745;
        }

        .error {
            color: red;
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>Sign Up</h2>
        <form id="signup-form">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>

            <div class="form-group">
                <label for="email">NYU Email:</label>
                <div class="email-group">
                    <input type="text" id="email-prefix" name="email-prefix" required placeholder="Enter your NetID">
                    <span>@nyu.edu</span>
                </div>
                <small class="error" id="email-error" style="display: none;">Email is required</small>
            </div>

            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>

            <div class="form-group">
                <label for="school">School:</label>
                <input type="text" id="school" name="school" required>
            </div>

            <div class="form-group">
                <label for="grade">Grade:</label>
                <select id="grade" name="grade" required>
                    <option value="" disabled selected>Select your grade</option>
                    <option value="Freshman">Freshman</option>
                    <option value="Sophomore">Sophomore</option>
                    <option value="Junior">Junior</option>
                    <option value="Senior">Senior</option>
                    <option value="Graduate">Graduate</option>
                </select>
            </div>

            <button type="submit">Sign Up</button>
        </form>

        <p id="response-message"></p>
    </div>

    <script>
        document.getElementById("signup-form").addEventListener("submit", function(event) {
            event.preventDefault();  // Prevent normal form submission

            let emailPrefix = document.getElementById("email-prefix").value.trim();
            let emailError = document.getElementById("email-error");

            if (emailPrefix === "") {
                emailError.style.display = "block";
                return;
            } else {
                emailError.style.display = "none";
            }

            let fullEmail = emailPrefix + "@nyu.edu";

            let formData = {
                name: document.getElementById("name").value,
                email: fullEmail,
                password: document.getElementById("password").value,
                school: document.getElementById("school").value,
                grade: document.getElementById("grade").value
            };

            fetch("http://127.0.0.1:8000/api/signup/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("response-message").innerText = data.message || "Registration successful!";
            })
            .catch(error => {
                document.getElementById("response-message").innerText = "Error: " + error;
            });
        });
    </script>

</body>
</html>