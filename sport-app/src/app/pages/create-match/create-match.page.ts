import { Component, OnInit } from '@angular/core';
import { Sport } from 'src/app/models/Sport';

@Component({
  selector: 'app-create-match',
  templateUrl: './create-match.page.html',
  styleUrls: ['./create-match.page.scss'],
})
export class CreateMatchPage implements OnInit {

  sportNuggets: Sport[] = []
  activeSport: string = ''
  tabNum: number = 1;
  constructor() { 
  }
  selectTab(action: boolean){
    if(action){
      if(this.tabNum==4){
        //TODO: finisher
      }else{
        this.tabNum += 1;
      }      
    }else{
      this.tabNum -= 1;
    }
  }

  selectSport(sportId: string){
    this.activeSport = sportId     
  }

  ngOnInit(): void {

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

}
