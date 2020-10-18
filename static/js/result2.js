var ctx = document.getElementById('pojinegaChart').getContext('2d');
var chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [ name1 +':'+per1+'%', name2+':'+per2+'%', name3+':'+per3+'%', name4+':'+per4+'%', name5+':'+per5+'%'],
    datasets: [
      {
      label: 'ポジティブツイートの割合',
      backgroundColor: ['#ff1493', '#1414ff', '#14ff63', '#ffff14', '#ffa600'],
      data: [per1, per2, per3, per4, per5]
    }
    ]
  },
  options: {
  }
});
