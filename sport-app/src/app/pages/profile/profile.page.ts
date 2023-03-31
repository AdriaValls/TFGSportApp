import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Location } from "@angular/common";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.page.html',
  styleUrls: ['./profile.page.scss'],
})
export class ProfilePage implements OnInit {

  bio: string= 'user bio... lorem...';
  selectedTab: string = 'upcoming';
  

  constructor(public router: Router, public route: ActivatedRoute, private location: Location) { 
    
  }
  ngOnInit() {
  }
  segmentChanged(ev: any) {
    console.log('Segment changed', ev);
  }
  selectTab(tabName: string){
    this.selectedTab = tabName;
  }

  goBack(): void {
    this.location.back();
  }


}
