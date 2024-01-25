"use strict";
$(document).ready(function () {
  const url =
    "https://raw.githubusercontent.com/ashhadulislam/JSON-Airports-India/master/airports.json";

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      const citiesWithCodes = data.airports.map((airport) => ({
        cityName: airport.city_name,
        IATACode: airport.IATA_code,
      }));

      populateCitiesList(citiesWithCodes, "cityInputFrom", "citiesListFrom");
      populateCitiesList(citiesWithCodes, "cityInputTo", "citiesListTo");
    })
    .catch((error) => {
      console.error("There was a problem fetching the data:", error);
    });

  function populateCitiesList(citiesWithCodes, inputId, dataListId) {
    const datalist = document.createElement("datalist");
    datalist.id = dataListId;

    citiesWithCodes.forEach((city) => {
      const option = document.createElement("option");
      option.value = `${city.cityName} (${city.IATACode})`;
      datalist.appendChild(option);
    });

    const existingDatalist = document.getElementById(dataListId);
    if (existingDatalist) {
      existingDatalist.parentNode.removeChild(existingDatalist);
    }

    document.body.appendChild(datalist);

    const cityInput = document.getElementById(inputId);
    cityInput.setAttribute("list", dataListId);

    cityInput.addEventListener("input", function () {
      const inputText = this.value.toLowerCase();
      const matchingCities = citiesWithCodes.filter(
        (city) =>
          city.cityName.toLowerCase().includes(inputText) ||
          city.IATACode.toLowerCase().includes(inputText)
      );

      showCities(matchingCities, dataListId);
    });

    function showCities(matchingCities, dataListId) {
      const datalist = document.createElement("datalist");
      datalist.id = dataListId;

      matchingCities.forEach((city) => {
        const option = document.createElement("option");
        option.value = `${city.cityName} (${city.IATACode})`;
        datalist.appendChild(option);
      });

      const existingDatalist = document.getElementById(dataListId);
      if (existingDatalist) {
        existingDatalist.parentNode.removeChild(existingDatalist);
      }

      document.body.appendChild(datalist);
      cityInput.setAttribute("list", dataListId);
    }
  }

  // code for form submission 
  $("form").submit(async function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Check if all fields are filled
    if (await validateForm()) {
      console.log("Form is valid, submitting...");

      // If validation is successful, submit the form using AJAX
      $.ajax({
        url: $(this).attr("action"),
        type: $(this).attr("method"),
        data: $(this).serialize(),
        success: function (response) {
          // Handle the success response as needed
          console.log("Form submitted successfully:", response);
          showSuccessMessage("/base");
        },
        error: function (error) {
          // Handle the error response as needed
          console.error("Error submitting form:", error);
          alert("Error submitting form. Please try again.");
        },
      });
    } else {
      console.log("Validation failed");
      // If validation fails, you can choose to show an error message or take other actions
      // For example, you can display an alert or customize the behavior
      alert("Validation failed. Please check the form.");
    }
  });

  // Function to validate the form
  async function validateForm() {
    const form = $("form")[0];
    const formElements = form.elements;

    for (let i = 0; i < formElements.length - 1; i++) {
      if (formElements[i].type !== "checkbox" && formElements[i].value === "") {
        // Display an alert or customize the behavior for unfilled fields
        alert("Please fill in all fields.");
        return false;
      }
    }

    // Check if the checkbox is checked
    if (!formElements["checkbox"].checked) {
      alert("Please agree to the terms and conditions.");
      return false;
    }

    return true;
  }

  // Function to show success message
  function showSuccessMessage() {
    Swal.fire({
      title: "Post Added Successfully!",
      icon: "success",
      showConfirmButton: false,
      timer: 1500,
    }).then((result) => {
      // Redirect to the specified URL after the Swal modal is closed
      if (result.dismiss === Swal.DismissReason.timer) {
        window.location.href = `/base`;
      }
    });
  }
});