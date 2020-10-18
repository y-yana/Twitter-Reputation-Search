var ctx = document.getElementById('pojinegaChart').getContext('2d');
var chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [ name1, name2, name3, name4, name5],
    datasets: [{
      backgroundColor: ['#ff9999', '#9e9eff', '#9effff', '#9eff9e', '#ffff9e'],
      data: [per1, per2, per3, per4, per5]
    }]
  },
  options: {}
});
