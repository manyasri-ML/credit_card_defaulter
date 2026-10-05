const form = document.getElementById("predictionForm");

const loading = document.getElementById("loading");
const result = document.getElementById("result");
const predictionText = document.getElementById("predictionText");


form.addEventListener("submit", async function (event) {

    event.preventDefault();


    // Show loading
    loading.classList.remove("hidden");
    result.classList.add("hidden");


    // Collect all 23 features
    const data = {

        // Personal Information
        LIMIT_BAL: Number(document.getElementById("LIMIT_BAL").value),
        CHILDREN: Number(document.getElementById("CHILDREN").value),
        EDUCATION: Number(document.getElementById("EDUCATION").value),
        MARRIAGE: Number(document.getElementById("MARRIAGE").value),
        AGE: Number(document.getElementById("AGE").value),

        // Payment Status
        PAY_0: Number(document.getElementById("PAY_0").value),
        PAY_2: Number(document.getElementById("PAY_2").value),
        PAY_3: Number(document.getElementById("PAY_3").value),
        PAY_4: Number(document.getElementById("PAY_4").value),
        PAY_5: Number(document.getElementById("PAY_5").value),
        PAY_6: Number(document.getElementById("PAY_6").value),

        // Bill Amounts
        BILL_AMT1: Number(document.getElementById("BILL_AMT1").value),
        BILL_AMT2: Number(document.getElementById("BILL_AMT2").value),
        BILL_AMT3: Number(document.getElementById("BILL_AMT3").value),
        BILL_AMT4: Number(document.getElementById("BILL_AMT4").value),
        BILL_AMT5: Number(document.getElementById("BILL_AMT5").value),
        BILL_AMT6: Number(document.getElementById("BILL_AMT6").value),

        // Payment Amounts
        PAY_AMT1: Number(document.getElementById("PAY_AMT1").value),
        PAY_AMT2: Number(document.getElementById("PAY_AMT2").value),
        PAY_AMT3: Number(document.getElementById("PAY_AMT3").value),
        PAY_AMT4: Number(document.getElementById("PAY_AMT4").value),
        PAY_AMT5: Number(document.getElementById("PAY_AMT5").value),
        PAY_AMT6: Number(document.getElementById("PAY_AMT6").value)
    };


    try {

        // Send data to FastAPI
        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        // Check response
        if (!response.ok) {
            throw new Error("Prediction request failed");
        }


        // Get response
        const resultData = await response.json();


        // Hide loading
        loading.classList.add("hidden");


        // Show result
        result.classList.remove("hidden");


        // Calculate probability
        const probability =
            resultData.default_probability * 100;


        // Display prediction
        predictionText.innerHTML = `
            ${resultData.prediction_label}
            <br>
            <small>
                Default Probability:
                ${probability.toFixed(2)}%
            </small>
        `;

    }


    catch (error) {

        loading.classList.add("hidden");

        result.classList.remove("hidden");

        predictionText.innerHTML =
            "Error: Could not connect to the prediction API.";

        console.error(error);
    }

});