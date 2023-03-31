import { Component, OnInit } from '@angular/core';
import { Sport } from 'src/app/models/Sport';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
})
export class HomePage implements OnInit {

  sportNuggets: Sport[] = []

  constructor() { }

  ngOnInit() {

    const sportsList: Sport[] = [
      { 
        name: 'futbol',
        icon: '../../../assets/icon/sports_soccer.svg'
      },
      { 
        name: 'basquet',
        icon: '../../../assets/icon/sports_basketball.svg'
      },
      { 
        name: 'tennis',
        icon: '../../../assets/icon/sports_tennis.svg'
      },
      { 
        name: 'volleyball',
        icon: '../../../assets/icon/sports_volleyball.svg'
      },

    ]
    this.sportNuggets = sportsList;

  }

  handleRefresh() {
    setTimeout(() => {
      // Any calls to load data go here
      //event.target.complete();
    }, 2);
  };

}
