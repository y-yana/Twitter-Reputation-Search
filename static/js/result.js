var ctx = document.getElementById('pojinegaChart').getContext('2d');

if (m_per == 0) {
  var chart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['positive(' + p_per + '%)', 'negative(' + n_per + '%)'],
      datasets: [{
        backgroundColor: ['#ff5ac8', '#2269e1'],
        data: [p_per, n_per]
      }]
    },
    options: {}
  });
} else {
  var chart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['ResultNone(' + m_per + '%)'],
      datasets: [{
        backgroundColor: ['#dcdddd'],
        data: [m_per]
      }]
    },
    options: {}
  });
};
