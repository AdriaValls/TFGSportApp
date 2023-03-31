import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-match-card',
  templateUrl: './match-card.component.html',
  styleUrls: ['./match-card.component.scss'],
})
export class MatchCardComponent  implements OnInit {

  constructor(public router: Router, public route: ActivatedRoute) { 
    
  }
  ngOnInit() {}

  gotoMatch() {
    this.router.navigate(['/tabs/match']);
  }
}
