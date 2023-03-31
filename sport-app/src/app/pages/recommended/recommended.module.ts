import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { RecommendedPageRoutingModule } from './recommended-routing.module';

import { RecommendedPage } from './recommended.page';
import { HeaderComponent } from 'src/app/components/header/header.component';
import { HeaderModule } from 'src/app/components/header/header.module';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RecommendedPageRoutingModule,
    HeaderModule     
  ],
  declarations: [RecommendedPage]
})
export class RecommendedPageModule {}
