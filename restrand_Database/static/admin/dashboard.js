document.addEventListener("DOMContentLoaded", function () {
    // Gender Proportion Chart
    const genderProportionCtx = document.getElementById("genderProportionChart").getContext("2d");
    new Chart(genderProportionCtx, {
        type: 'doughnut',
        data: {
            labels: ['Male', 'Female'],
            datasets: [{
                data: [67, 33],
                backgroundColor: ['blue', '#ff57b2'],
            }]
        }
    });

    // Distribution of Grades
    const distributionGradesCtx = document.getElementById("distributionGradesChart").getContext("2d");
    new Chart(distributionGradesCtx, {
        type: 'bar',
        data: {
            labels: ['77.5', '80.0', '82.5', '85.0', '87.5', '90.0', '92.5', '95.0'],
            datasets: [{
                label: 'Grades',
                data: [1, 0, 0, 0, 0, 0, 0, 0],
                backgroundColor: '#4b49ac',
            }]
        }
    });

    // Student Distribution
    const studentDistributionCtx = document.getElementById("studentDistributionChart").getContext("2d");
    new Chart(studentDistributionCtx, {
        type: 'bar',
        data: {
            labels: ['STEM', 'ABM', 'HUMSS', 'GAS', 'TVL'],
            datasets: [{
                label: 'Number of Students',
                data: [9693, 867, 1120, 69, 1434],
                backgroundColor: '#4b49ac',
            }]
        }
    });

    // Gender Distribution
    const genderDistributionCtx = document.getElementById("genderDistributionChart").getContext("2d");
    new Chart(genderDistributionCtx, {
        type: 'bar',
        data: {
            labels: ['STEM', 'ABM', 'HUMSS', 'GAS', 'TVL'],
            datasets: [
                {
                    label: 'Male',
                    data: [500, 400, 300, 200, 100],
                    backgroundColor: '#4b49ac'
                },
                {
                    label: 'Female',
                    data: [300, 200, 100, 50, 75],
                    backgroundColor: '#ff57b2'
                }
            ]
        }
    });

    // GPA Distribution
    const gpaDistributionCtx = document.getElementById("gpaDistributionChart").getContext("2d");
    new Chart(gpaDistributionCtx, {
        type: 'bar',
        data: {
            labels: ['1.5 - 1.0', '2.0 - 1.5', '2.5 - 2.0', '3.0 - 2.5', '3.5 - 3.0'],
            datasets: [{
                label: 'Number of Students',
                data: [200, 300, 400, 300, 150],
                backgroundColor: '#4b49ac',
            }]
        }
    });

    // GPA vs Strand
    const gpaVsStrandCtx = document.getElementById("gpaVsStrandChart").getContext("2d");
    new Chart(gpaVsStrandCtx, {
        type: 'bar',
        data: {
            labels: ['STEM', 'ABM', 'HUMSS', 'GAS', 'TVL'],
            datasets: [{
                label: 'Average GPA',
                data: [3.5, 3.5, 3.0, 2.5, 2.0],
                backgroundColor: '#4b49ac',
            }]
        }
    });
});

function toggleDropdown() {
    const dropdown = document.getElementById('profileDropdown');
    dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
}

// Close the dropdown if clicked outside
document.addEventListener('click', function(event) {
    const dropdown = document.getElementById('profileDropdown');
    const isClickInside = dropdown.contains(event.target) || event.target.closest('.nav-item');

    if (!isClickInside && dropdown.style.display === 'block') {
        dropdown.style.display = 'none';
    }
});

// Change color on click
function setActive(element) {
    // Reset color for all items
    document.querySelectorAll('.dropdown-item').forEach(item => item.style.color = '#333');
    
    // Set the clicked item color to #1f3b77
    element.style.color = '#1f3b77';
}


