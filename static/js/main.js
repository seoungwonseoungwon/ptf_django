const ctx = document.getElementById('yongsan');
  
  const labels = [
    {% for cd in yongsan_datas %}
    '{{ cd.restaurant }}',
    {% endfor %}
  ]
  
  const pop_data = [
    {% for cd in yongsan_datas %}
    {{ cd.name_count }},
    {% endfor %}
  
  ]
  
  const data = {
    labels: labels,
    datasets: [{
      label: '냥냥',
      data: pop_data,
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(255, 205, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(201, 203, 207, 0.2)'
      ],
      borderColor: [
        'rgb(255, 99, 132)',
        'rgb(255, 159, 64)',
        'rgb(255, 205, 86)',
        'rgb(75, 192, 192)',
        'rgb(54, 162, 235)',
        'rgb(153, 102, 255)',
        'rgb(201, 203, 207)'
      ],
      borderWidth: 1
    }]
  };
  
  const config = {
    type: 'bar',
    data: data,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    },
  };
  
  new Chart(ctx, config)