var ctx = document.getElementById('pojinegaChart').getContext('2d');
var chart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['positive', 'negative'],
    datasets: [{
      backgroundColor: ['#ff5ac8', '#2269e1'],
      data: [p_per, n_per]
    }]
  },
  options: {}
});
