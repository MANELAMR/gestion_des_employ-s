new Morris.Line({
    // ID of the element in which to draw the chart.
    element: 'myfirstchart',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: [
      { year: '2008', value: 20 },
      { year: '2009', value: 10 },
      { year: '2010', value: 5 },
      { year: '2011', value: 5 },
      { year: '2012', value: 20 }
    ],
    // The name of the data record attribute that contains x-values.
    xkey: 'year',
    // A list of names of data record attributes that contain y-values.
    ykeys: ['value'],
    // Labels for the ykeys -- will be displayed when you hover over the
    // chart.
    labels: ['Value']
  });Morris.Donut({
    element: 'donut-example',
    data: [
      {label: "technicien supérieure", value: 12},
      {label: "comptable", value: 30},
      {label: "administrateur", value: 20},
      {label: "secrrtaire", value: 20},
      {label: "responsable de traitementc", value: 20},
      {label: "agent de securite", value: 20},
      {label: "enseignant", value: 20},
      {label: "responsable de laboratoire", value: 20},






    ]
  });