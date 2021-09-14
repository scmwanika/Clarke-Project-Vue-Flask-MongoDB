// Vue instance
new Vue({
  // the data property
  el: "#table-info",
  data() {
    return {
      reviewList: [
        {
          id: 1,
          name: 'Corporate Events',
          rating: 'Venue',
          comment: 'Games and sports',
          reviewDate: '',
        },
        {
          id: 2,
          name: 'Corporate Events',
          rating: 'Venue',
          comment: 'Games and sports',
          reviewDate: '',
        },
        {
          id: 3,
          name: 'Corporate Events',
          rating: 'Venue',
          comment: 'Games and sports',
          reviewDate: '',
        },
        {
          id: 4,
          name: 'Corporate Events',
          rating: 'Venue',
          comment: 'Games and sports',
          reviewDate: '',
        },
      ],
    };
  },
  // the methods property
  methods: {
    power: function () {
      this.image = !this.image
    }
  }
});