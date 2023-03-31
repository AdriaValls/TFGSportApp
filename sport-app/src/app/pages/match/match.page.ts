import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Location } from "@angular/common";

@Component({
  selector: 'app-match',
  templateUrl: './match.page.html',
  styleUrls: ['./match.page.scss'],
})
export class MatchPage implements OnInit {

  selectedTab: string = 'info';

  team1: string[] = ['player1','player2']
  team2: string[] = ['player3','player4']

  constructor(public router: Router, public route: ActivatedRoute, private location: Location) { }

  ngOnInit() {
  }
  
  goBack(): void {
    this.location.back();
  }
  segmentChanged(ev: any) {
    console.log('Segment changed', ev);
  }
  selectTab(tabName: string){
    this.selectedTab = tabName;
  }
}
