# Clidrive backend — database schema

Generated from `/Users/felipeguzman/Documents/Clidrive/backend/database/schema.prisma` by `gen_db_schema.py`. 110 models, 3 views, 94 enums. Regenerate after backend changes rather than editing by hand.

## Index

[ClientCallsNormalized](#clientcallsnormalized), [GenericCache](#genericcache), [PrismaAddress](#prismaaddress), [PrismaAffiliate](#prismaaffiliate), [PrismaAffiliateCampaignCostRules](#prismaaffiliatecampaigncostrules), [PrismaAffiliateCampaignCosts](#prismaaffiliatecampaigncosts), [PrismaAffiliateCampaigns](#prismaaffiliatecampaigns), [PrismaAiVoiceCall](#prismaaivoicecall), [PrismaAlerts](#prismaalerts), [PrismaAppraisalTradeIn](#prismaappraisaltradein), [PrismaBankAccount](#prismabankaccount), [PrismaBelenderDocuments](#prismabelenderdocuments), [PrismaC2CDealMetrics](#prismac2cdealmetrics), [PrismaCarDeliveries](#prismacardeliveries), [PrismaCarfaxVehicleEquivalence](#prismacarfaxvehicleequivalence), [PrismaCatalogueVehicle](#prismacataloguevehicle), [PrismaCatalogueVehicleAd](#prismacataloguevehiclead), [PrismaCatalogueVehicleAdSource](#prismacataloguevehicleadsource), [PrismaCatalogueVehicleClientHistory](#prismacataloguevehicleclienthistory), [PrismaCatalogueVehicleDocument](#prismacataloguevehicledocument), [PrismaCatalogueVehicleExternalInfo](#prismacataloguevehicleexternalinfo), [PrismaCatalogueVehicleExtra](#prismacataloguevehicleextra), [PrismaCatalogueVehicleImage](#prismacataloguevehicleimage), [PrismaCatalogueVehicleInspection](#prismacataloguevehicleinspection), [PrismaCatalogueVehicleJatoData](#prismacataloguevehiclejatodata), [PrismaCatalogueVehicleManagedAds](#prismacataloguevehiclemanagedads), [PrismaCatalogueVehicleMarketValuations](#prismacataloguevehiclemarketvaluations), [PrismaCatalogueVehicleNotificationHistory](#prismacataloguevehiclenotificationhistory), [PrismaCatalogueVehiclePerformance](#prismacataloguevehicleperformance), [PrismaCatalogueVehicleService](#prismacataloguevehicleservice), [PrismaCatalogueVehicleTitleReservation](#prismacataloguevehicletitlereservation), [PrismaCatalogueVehiclesRepricing](#prismacataloguevehiclesrepricing), [PrismaCatalogueVehiclesStatusTransitions](#prismacataloguevehiclesstatustransitions), [PrismaCertification](#prismacertification), [PrismaCertificationDocument](#prismacertificationdocument), [PrismaCertificationSchedulerSlot](#prismacertificationschedulerslot), [PrismaCertificationSchedulerTemplate](#prismacertificationschedulertemplate), [PrismaChangelog](#prismachangelog), [PrismaChangelogItem](#prismachangelogitem), [PrismaClientBlacklist](#prismaclientblacklist), [PrismaClientCalls](#prismaclientcalls), [PrismaClientCoOwner](#prismaclientcoowner), [PrismaClientDocument](#prismaclientdocument), [PrismaConfiguration](#prismaconfiguration), [PrismaCustomer](#prismacustomer), [PrismaDealCollectionsStatus](#prismadealcollectionsstatus), [PrismaDealNote](#prismadealnote), [PrismaDealNoteAttachment](#prismadealnoteattachment), [PrismaDealStage](#prismadealstage), [PrismaDealStageTransition](#prismadealstagetransition), [PrismaDealValuation](#prismadealvaluation), [PrismaDocumentAnalyses](#prismadocumentanalyses), [PrismaExternalVehicleProvider](#prismaexternalvehicleprovider), [PrismaFinancialAggregationProducts](#prismafinancialaggregationproducts), [PrismaFinancialAggregationTransactions](#prismafinancialaggregationtransactions), [PrismaFinancialAggregations](#prismafinancialaggregations), [PrismaFinancingRequest](#prismafinancingrequest), [PrismaGatewayPayment](#prismagatewaypayment), [PrismaInterest](#prismainterest), [PrismaInterestAi](#prismainterestai), [PrismaInterestFinancialService](#prismainterestfinancialservice), [PrismaInterestMetrics](#prismainterestmetrics), [PrismaInterestService](#prismainterestservice), [PrismaMultipublisherError](#prismamultipublishererror), [PrismaNote](#prismanote), [PrismaNoteAttachment](#prismanoteattachment), [PrismaNpsForm](#prismanpsform), [PrismaNpsSubmission](#prismanpssubmission), [PrismaOAuthPkceSession](#prismaoauthpkcesession), [PrismaOAuthToken](#prismaoauthtoken), [PrismaOffer](#prismaoffer), [PrismaPaymentBreakdowns](#prismapaymentbreakdowns), [PrismaPreoffer](#prismapreoffer), [PrismaPreofferProposal](#prismapreofferproposal), [PrismaProvince](#prismaprovince), [PrismaProvinceEquivalence](#prismaprovinceequivalence), [PrismaPuntoAi](#prismapuntoai), [PrismaPurchaseDiscounts](#prismapurchasediscounts), [PrismaPurchaseTransactions](#prismapurchasetransactions), [PrismaRequestLogs](#prismarequestlogs), [PrismaReservation](#prismareservation), [PrismaRespondioAssignees](#prismarespondioassignees), [PrismaRespondioAttachments](#prismarespondioattachments), [PrismaRespondioContacts](#prismarespondiocontacts), [PrismaRespondioMessages](#prismarespondiomessages), [PrismaRespondioTagEvents](#prismarespondiotagevents), [PrismaService](#prismaservice), [PrismaSubmission](#prismasubmission), [PrismaSubmissionDocument](#prismasubmissiondocument), [PrismaSubmissionStatusTransitions](#prismasubmissionstatustransitions), [PrismaUser](#prismauser), [PrismaVehicle](#prismavehicle), [PrismaVehicleColor](#prismavehiclecolor), [PrismaVehicleMake](#prismavehiclemake), [PrismaVehicleModel](#prismavehiclemodel), [PrismaVehicleVersion](#prismavehicleversion), [PrismaVehicleYear](#prismavehicleyear), [appraisals](#appraisals), [asnef_equifax](#asnef_equifax), [carfax](#carfax), [clients](#clients), [credentials](#credentials), [deal_stages_updates](#deal_stages_updates), [deals](#deals), [ganvam](#ganvam), [installments](#installments), [invoices](#invoices), [motor_es](#motor_es), [motor_es_makes](#motor_es_makes), [motor_es_models](#motor_es_models), [motor_es_years](#motor_es_years), [payment_plans](#payment_plans), [payments](#payments)

## Models and views

### ClientCallsNormalized (view, table: `client_calls_normalized`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | unique |
| uuid | String |  |
| buyerClientId | Int |  |
| sellerClientId | Int |  |
| interestId | Int? |  |
| providerMetadata | Json? |  |
| status | String |  |
| startedAt | DateTime? |  |
| endedAt | DateTime? |  |
| durationSeconds | Int? |  |
| webhookReceivedAt | DateTime? |  |
| recordingFileKey | String? |  |
| transcription | String? |  |
| createdAt | DateTime |  |
| updatedAt | DateTime |  |
| transcriptionStructured | String? |  |
| buyer_client | clients | relation |
| seller_client | clients | relation |
| interest | PrismaInterest? | relation |

### GenericCache (model, table: `generic_caches`)

| Field | Type | Attributes |
|---|---|---|
| id | String | PK, default=dbgenerated("gen_random_uuid()") |
| key | String |  |
| type | String |  |
| data | String |  |
| expires_at | DateTime |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |

### PrismaAddress (model, table: `addresses`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| route | String? |  |
| street_number | String? |  |
| postal_code | String? |  |
| city | String? |  |
| province | String? |  |
| domicile | String? |  |
| complete | String? |  |
| house_type | house_types_type? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| customer_id | Int? |  |
| clients | clients[] | relation |
| customer | PrismaCustomer? | relation |
| car_delivery | PrismaCarDeliveries? |  |
| client_co_owner | PrismaClientCoOwner? |  |

### PrismaAffiliate (model, table: `affiliates`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| biddings | affiliate_bidding_type[] |  |
| name | String |  |
| deal_won_webhook_url | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deals | deals[] |  |
| credentials | credentials[] |  |
| PrismaAffiliateCampaigns | PrismaAffiliateCampaigns[] |  |

### PrismaAffiliateCampaignCostRules (model, table: `affiliate_campaign_cost_rules`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| activated_at | DateTime? |  |
| deactivated_at | DateTime? |  |
| affiliate_campaign_id | Int |  |
| min_car_years | Int? |  |
| max_car_years | Int? |  |
| min_loan_amount | Decimal? |  |
| max_loan_amount | Decimal? |  |
| min_asked_amount | Decimal? |  |
| max_asked_amount | Decimal? |  |
| cost_amount | Decimal |  |
| cost_currency | currency |  |
| affiliate_campaign | PrismaAffiliateCampaigns | relation |
| campaign_costs | PrismaAffiliateCampaignCosts[] |  |

### PrismaAffiliateCampaignCosts (model, table: `affiliate_campaign_costs`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deal_id | Int | unique |
| cost_currency | currency? |  |
| cost_amount | Decimal? |  |
| cost_rule_id | Int? |  |
| campaign_id | Int |  |
| deal | deals | relation |
| cost_rule | PrismaAffiliateCampaignCostRules? | relation |
| campaign | PrismaAffiliateCampaigns | relation |

### PrismaAffiliateCampaigns (model, table: `affiliate_campaigns`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| activated_at | DateTime? |  |
| deactivated_at | DateTime? |  |
| affiliate_id | Int |  |
| name | String |  |
| bidding | affiliate_bidding_type |  |
| affiliate | PrismaAffiliate | relation |
| cost_rules | PrismaAffiliateCampaignCostRules[] |  |
| costs | PrismaAffiliateCampaignCosts[] |  |

### PrismaAiVoiceCall (model, table: `ai_voice_calls`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| call_id | String | unique |
| source | String |  |
| event | String |  |
| agent_id | String |  |
| agent_version | Int? |  |
| call_type | ai_voice_call_type |  |
| direction | ai_voice_call_direction? |  |
| call_status | ai_voice_call_status |  |
| disconnection_reason | String? |  |
| from_number | String? |  |
| to_number | String? |  |
| started_at | DateTime |  |
| ended_at | DateTime? |  |
| duration_seconds | Int |  |
| successful | Boolean? |  |
| user_sentiment | ai_voice_call_sentiment? |  |
| in_voicemail | Boolean? |  |
| summary | String? |  |
| custom_analysis_data | Json? |  |
| recording_url | String? |  |
| public_log_url | String? |  |
| transcript | String? |  |
| transcript_object | Json? |  |
| cost | Json? |  |
| latency | Json? |  |
| llm_token_usage | Json? |  |
| tool_calls | Json? |  |
| metadata | Json? |  |
| dynamic_variables | Json? |  |
| collected_dynamic_variables | Json? |  |
| opt_out_sensitive_data_storage | Boolean? |  |
| data_storage_setting | ai_voice_call_data_storage_setting? |  |
| received_at | DateTime |  |
| raw | Json? |  |
| interest_id | Int |  |
| catalogue_vehicle_id | Int |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| interest | PrismaInterest | relation |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |

### PrismaAlerts (model, table: `alerts`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| license_plate | String | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| expires_at | DateTime |  |
| data | Json |  |

### PrismaAppraisalTradeIn (model, table: `appraisals_trade_in`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| client_id | Int |  |
| external_id | String |  |
| license_plate | String |  |
| kilometers | Int |  |
| make | String |  |
| model | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| data | Json |  |
| clients | clients | relation |

### PrismaBankAccount (model, table: `bank_accounts`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| iban | String |  |
| bic_swift | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| customer_id | Int |  |
| customer | PrismaCustomer | relation |

### PrismaBelenderDocuments (model, table: `belender_documents`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| type | belender_document_type |  |
| data | Json |  |
| identification_number | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |

### PrismaC2CDealMetrics (view, table: `c2c_deal_metrics`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | unique |
| uuid | String | unique |
| license_plate | String? |  |
| total_discounts | Decimal? |  |
| ad_price | Decimal? |  |
| purchase_price | Decimal? |  |
| preparation_expenses | Decimal? |  |
| delivery_expenses | Decimal? |  |
| premium_warranty | Decimal? |  |
| commission_fee_amount | Decimal? |  |
| gpu | Decimal? |  |
| gpus | Decimal? |  |
| metal_margin | Decimal? |  |
| total_selling_price | Decimal? |  |
| reservation_amount | Decimal? |  |
| total_financed | Decimal? |  |
| total_transactions | Decimal? |  |
| total_revenues | Decimal? |  |

### PrismaCarDeliveries (model, table: `car_deliveries`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deal_id | Int? | unique |
| interest_id | Int? | unique |
| address_id | Int? | unique |
| delivery_date | DateTime? |  |
| provider | delivery_provider_type? |  |
| contract | delivery_signed_doc_status | default=PENDING |
| mandate | delivery_signed_doc_status | default=PENDING |
| certification | delivery_signed_doc_status | default=PENDING |
| photo_consent | delivery_signed_doc_status | default=PENDING |
| invoice | delivery_requested_doc_status | default=NOT_REQUESTED |
| professional_justification | delivery_sent_doc_status | default=PENDING |
| cleaning | delivery_cleaning_status | default=NOT_CLEANED |
| deal | deals? | relation |
| address | PrismaAddress? | relation |
| interest | PrismaInterest? | relation |

### PrismaCarfaxVehicleEquivalence (model, table: `carfax_vehicle_equivalences`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| carfax_name | String | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| vehicle_make_id | Int |  |
| vehicle_model_id | Int |  |
| make | PrismaVehicleMake | relation |
| model | PrismaVehicleModel | relation |

### PrismaCatalogueVehicle (model, table: `catalogue_vehicles`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| license_plate | String? | unique |
| vin | String? | unique |
| mileage | Decimal? |  |
| power | Decimal? |  |
| power_kw | Decimal? |  |
| fiscal_power | Decimal? |  |
| eu_vehicle_category | String? |  |
| number_of_doors | Int? |  |
| number_of_seats | Int? |  |
| combustible_type | combustible_type? |  |
| gearbox_type | gearbox_type? |  |
| drivetrain_type | drivetrain_type? |  |
| timing_belt_type | timing_belt_type? |  |
| energy_classification_type | energy_classification_type? |  |
| trasferable | Boolean? |  |
| manufacture_year | Int? |  |
| year_registration | Int? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| status | catalogue_vehicles_status_type | default=NEW |
| sub_status | catalogue_vehicles_sub_status_type | default=PENDING_APPRAISAL |
| status_transitions | PrismaCatalogueVehiclesStatusTransitions[] |  |
| registration_date | DateTime? |  |
| has_second_key | Boolean? |  |
| has_maintenance_log | Boolean? |  |
| vat_rates | vat_rate_type? |  |
| ad_price_amount | Decimal? |  |
| ad_price_currency | currency? |  |
| purchase_price_amount | Decimal? |  |
| purchase_price_currency | currency? |  |
| target_purchase_price_amount | Decimal? |  |
| target_purchase_price_currency | currency? |  |
| original_price_amount | Decimal? |  |
| original_price_currency | currency? |  |
| selling_financed_price_amount | Decimal? |  |
| selling_financed_price_currency | currency? |  |
| selling_cash_price_amount | Decimal? |  |
| selling_cash_price_currency | currency? |  |
| selling_offer_price_amount | Decimal? |  |
| selling_offer_price_currency | currency? |  |
| target_selling_financed_price_amount | Decimal? |  |
| target_selling_financed_price_currency | currency? |  |
| target_selling_cash_price_amount | Decimal? |  |
| target_selling_cash_price_currency | currency? |  |
| is_imported | Boolean? |  |
| published_at | DateTime? |  |
| unpublished_at | DateTime? |  |
| ext_id | String? | unique |
| extra_info | String? |  |
| brand_warranty_expired_at | DateTime? |  |
| vehicle_type | vehicle_type? |  |
| notifications_config | Json | default="{\"isRepricingPaused\":false,\"isAvailabilityPaused\":false}" |
| price_to_market_deviation | Decimal? |  |
| price_to_market_amount | Decimal? |  |
| price_to_market_label | price_to_market_label_type? |  |
| engine_displacement | Int? |  |
| last_vehicle_inspection_date | DateTime? |  |
| next_vehicle_inspection_date | DateTime? |  |
| ganvam_price_amount | Decimal? |  |
| ganvam_price_currency | currency? |  |
| ganvam_price_to_market_deviation | Decimal? |  |
| marketplace_offer_until | DateTime? |  |
| bodywork_type | bodywork_type? |  |
| interests_count | Int | default=0 |
| ad_views_count | Int | default=0 |
| in_balance | Boolean | default=false |
| installment_amount | Decimal? |  |
| financing_installments_info | Json? |  |
| number_of_owners | Int? |  |
| business_type | catalogue_vehicle_business_type | default=C2B2C |
| jato_instance_id | String? |  |
| jato_version_id | String? |  |
| has_carfax_alert | Boolean? |  |
| processor_user_id | Int? |  |
| vehicle_make_id | Int? |  |
| vehicle_model_id | Int? |  |
| vehicle_version_id | Int? |  |
| vehicle_year_id | Int? |  |
| vehicle_color_id | Int? |  |
| province_id | Int? |  |
| client_id | Int? |  |
| processor_user | PrismaUser? | relation |
| vehicle_make | PrismaVehicleMake? | relation |
| vehicle_model | PrismaVehicleModel? | relation |
| vehicle_version | PrismaVehicleVersion? | relation |
| vehicle_year | PrismaVehicleYear? | relation |
| vehicle_color | PrismaVehicleColor? | relation |
| province | PrismaProvince? | relation |
| client | clients? | relation |
| extras | PrismaCatalogueVehicleExtra[] | relation |
| performance | PrismaCatalogueVehiclePerformance? |  |
| title_reservation | PrismaCatalogueVehicleTitleReservation? |  |
| seller_ad | PrismaCatalogueVehicleAd? |  |
| inspection | PrismaCatalogueVehicleInspection? |  |
| deals | deals[] |  |
| managed_ads | PrismaCatalogueVehicleManagedAds[] |  |
| repricing | PrismaCatalogueVehiclesRepricing[] |  |
| market_valuation | PrismaCatalogueVehicleMarketValuations? |  |
| notification_history | PrismaCatalogueVehicleNotificationHistory[] | relation |
| images | PrismaCatalogueVehicleImage[] | relation |
| jatoData | PrismaCatalogueVehicleJatoData[] | relation |
| documents | PrismaCatalogueVehicleDocument[] |  |
| purchase_transactions | PrismaPurchaseTransactions[] |  |
| payment_breakdowns | PrismaPaymentBreakdowns[] |  |
| multipublisherErrors | PrismaMultipublisherError[] |  |
| externalInfo | PrismaCatalogueVehicleExternalInfo? |  |
| interests | PrismaInterest[] |  |
| notes | PrismaNote[] | relation |
| client_history | PrismaCatalogueVehicleClientHistory[] |  |
| catalogue_vehicle_services | PrismaCatalogueVehicleService[] |  |
| document_analyses | PrismaDocumentAnalyses[] |  |
| nps_submissions | PrismaNpsSubmission[] |  |
| certifications | PrismaCertification[] |  |
| ai_voice_calls | PrismaAiVoiceCall[] |  |

### PrismaCatalogueVehicleAd (model, table: `catalogue_vehicle_ads`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| link | String? |  |
| description | String? |  |
| seller_name | String? |  |
| seller_first_surname | String? |  |
| seller_second_surname | String? |  |
| seller_phone | String? |  |
| seller_second_phone | String? |  |
| seller_email | String? |  |
| published_at | DateTime? |  |
| publication_updated_at | DateTime? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicle_id | Int | unique |
| catalogue_vehicle_ad_source_id | Int |  |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |
| catalogue_vehicle_ad_source | PrismaCatalogueVehicleAdSource | relation |

### PrismaCatalogueVehicleAdSource (model, table: `catalogue_vehicle_ad_sources`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | catalogue_vehicle_ad_source_type | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicle_ads | PrismaCatalogueVehicleAd[] |  |
| PrismaCatalogueVehicleManagedAds | PrismaCatalogueVehicleManagedAds[] |  |

### PrismaCatalogueVehicleClientHistory (model, table: `catalogue_vehicle_client_history`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| client_id | Int |  |
| catalogue_vehicle_id | Int |  |
| mileage | Int? |  |
| province_id | Int? |  |
| vehicle_color_id | Int? |  |
| processor_user_id | Int? |  |
| ad_price_amount | Decimal? |  |
| ad_price_currency | currency? |  |
| purchase_price_amount | Decimal? |  |
| purchase_price_currency | currency? |  |
| target_purchase_price_amount | Decimal? |  |
| target_purchase_price_currency | currency? |  |
| selling_cash_price_amount | Decimal? |  |
| selling_cash_price_currency | currency? |  |
| selling_financed_price_amount | Decimal? |  |
| selling_financed_price_currency | currency? |  |
| target_selling_cash_price_amount | Decimal? |  |
| target_selling_cash_price_currency | currency? |  |
| target_selling_financed_price_amount | Decimal? |  |
| target_selling_financed_price_currency | currency? |  |
| status | catalogue_vehicles_status_type |  |
| sub_status | catalogue_vehicles_sub_status_type |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| client | clients | relation |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |
| province | PrismaProvince? | relation |
| vehicle_color | PrismaVehicleColor? | relation |
| processor_user | PrismaUser? | relation |

### PrismaCatalogueVehicleDocument (model, table: `catalogue_vehicle_documents`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| document_path | String |  |
| type | catalogue_vehicle_document_type |  |
| catalogue_vehicle_id | Int |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deleted_at | DateTime? |  |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |
| certification_documents | PrismaCertificationDocument[] |  |

### PrismaCatalogueVehicleExternalInfo (model, table: `catalogue_vehicle_external_info`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| ad_id | String |  |
| ad_url | String? |  |
| external_vehicle_provider_id | Int |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicle_id | Int | unique |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |
| external_vehicle_provider | PrismaExternalVehicleProvider | relation |

### PrismaCatalogueVehicleExtra (model, table: `catalogue_vehicle_extras`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | String | unique |
| slug | String | unique |
| category_type | vehicle_extra_category_type |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicles | PrismaCatalogueVehicle[] | relation |

### PrismaCatalogueVehicleImage (model, table: `catalogue_vehicle_images`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| image_path | String? |  |
| image_paths | Json | default="{}" |
| source | catalogue_vehicle_image_source |  |
| catalogue_vehicle_id | Int |  |
| order | Int | default=0 |
| sumauto_id | String? |  |
| cochesnet_id | String? |  |
| wallapop_id | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |

### PrismaCatalogueVehicleInspection (model, table: `catalogue_vehicle_inspections`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| is_approved | Boolean |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| certifier_user_id | Int |  |
| catalogue_vehicle_id | Int | unique |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |
| certifier_user | PrismaUser | relation |

### PrismaCatalogueVehicleJatoData (model, table: `catalogue_vehicle_jato_data`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| content | String |  |
| type | catalogue_vehicle_jato_data_type |  |
| catalogue_vehicle_id | Int |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |

### PrismaCatalogueVehicleManagedAds (model, table: `catalogue_vehicle_managed_ads`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| link | String |  |
| external_id | String? |  |
| published_at | DateTime? |  |
| catalogue_vehicle_id | Int |  |
| catalogue_vehicle_ad_source_id | Int |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicles | PrismaCatalogueVehicle | relation |
| catalogue_vehicle_ad_source | PrismaCatalogueVehicleAdSource | relation |

### PrismaCatalogueVehicleMarketValuations (model, table: `catalogue_vehicle_market_valuations`)

| Field | Type | Attributes |
|---|---|---|
| source | catalogue_vehicle_ad_source_type? |  |
| ad_price_amount | Decimal? |  |
| ad_price_currency | currency? |  |
| market_price_amount | Decimal? |  |
| market_price_currency | currency? |  |
| price_to_market_type | price_to_market_types? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| catalogue_vehicle_id | Int | PK |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |

### PrismaCatalogueVehicleNotificationHistory (model, table: `catalogue_vehicle_notification_history`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| catalogue_vehicle_id | Int |  |
| notification_type | catalogue_vehicle_notification_type |  |
| repricing_id | Int? | unique |
| created_at | DateTime | default=now() |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |
| repricing | PrismaCatalogueVehiclesRepricing? | relation |

### PrismaCatalogueVehiclePerformance (model, table: `catalogue_vehicle_performances`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| fuel_tank_capacity_amount | Decimal? |  |
| fuel_tank_capacity_unit | capacity_unit? |  |
| avg_fuel_consumption_amount | Decimal? |  |
| avg_fuel_consumption_unit | consumption_unit? |  |
| avg_electric_consumption_amount | Decimal? |  |
| avg_electric_consumption_unit | consumption_unit? |  |
| electric_range_wltp_amount | Decimal? |  |
| electric_range_wltp_unit | length_unit? |  |
| battery_capacity_amount | Decimal? |  |
| battery_capacity_unit | capacity_unit? |  |
| charging_time_amount | Decimal? |  |
| charging_time_unit | time_unit? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicle_id | Int | unique |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |

### PrismaCatalogueVehicleService (model, table: `catalogue_vehicle_services`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| catalogue_vehicle_id | Int |  |
| service_id | Int |  |
| price_amount | Decimal? |  |
| price_currency | currency? |  |
| created_at | DateTime | default=now() |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |
| service | PrismaService | relation |

### PrismaCatalogueVehicleTitleReservation (model, table: `catalogue_vehicle_title_reservations`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| financier_name | String? |  |
| contract_number | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicle_id | Int | unique |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |

### PrismaCatalogueVehiclesRepricing (model, table: `catalogue_vehicles_repricing`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| catalogue_vehicle_id | Int |  |
| purchase_price_amount | Decimal? |  |
| purchase_price_currency | currency? |  |
| selling_financed_price_amount | Decimal? |  |
| selling_financed_price_currency | currency? |  |
| selling_cash_price_amount | Decimal? |  |
| selling_cash_price_currency | currency? |  |
| selling_offer_price_amount | Decimal? |  |
| selling_offer_price_currency | currency? |  |
| author_id | Int? |  |
| created_at | DateTime | default=now() |
| reason | String? |  |
| type | repricing_type |  |
| author | PrismaUser? | relation |
| catalogue_vehicles | PrismaCatalogueVehicle | relation |
| notification_history | PrismaCatalogueVehicleNotificationHistory? |  |

### PrismaCatalogueVehiclesStatusTransitions (model, table: `catalogue_vehicles_status_transitions`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| catalogue_vehicle_id | Int |  |
| current_status | catalogue_vehicles_status_type |  |
| previous_status | catalogue_vehicles_status_type? |  |
| current_sub_status | catalogue_vehicles_sub_status_type |  |
| previous_sub_status | catalogue_vehicles_sub_status_type? |  |
| author_id | Int? |  |
| created_at | DateTime | default=now() |
| reason | String? |  |
| started_at | DateTime? | default=now() |
| finished_at | DateTime? |  |
| author | PrismaUser? | relation |
| catalogue_vehicles | PrismaCatalogueVehicle | relation |

### PrismaCertification (model, table: `certifications`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| certifier_id | Int |  |
| seller_id | Int |  |
| interest_id | Int |  |
| catalogue_vehicle_id | Int |  |
| status | certification_status | default=SCHEDULED |
| reason | String? |  |
| cancelled_at | DateTime? |  |
| cancelled_by_id | Int? |  |
| first_reminder_sent | Boolean | default=false |
| second_reminder_sent | Boolean | default=false |
| start_at | DateTime |  |
| end_at | DateTime |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| seller_phone | String? |  |
| seller_name | String? |  |
| certifier | PrismaUser | relation |
| cancelled_by | PrismaUser? | relation |
| seller | clients | relation |
| interest | PrismaInterest | relation |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |
| certification_documents | PrismaCertificationDocument[] |  |

### PrismaCertificationDocument (model, table: `certification_documents`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| certification_id | Int |  |
| catalogue_vehicle_document_id | Int |  |
| certification | PrismaCertification | relation |
| catalogue_vehicle_document | PrismaCatalogueVehicleDocument | relation |

### PrismaCertificationSchedulerSlot (model, table: `certification_scheduler_slots`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| certifier_id | Int |  |
| start_at | DateTime |  |
| end_at | DateTime |  |
| template_id | Int? |  |
| certifier | PrismaUser | relation |
| template | PrismaCertificationSchedulerTemplate? | relation |

### PrismaCertificationSchedulerTemplate (model, table: `certification_scheduler_templates`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | String |  |
| template_config | Json |  |
| is_active | Boolean | default=true |
| created_at | DateTime | default=now() |
| slots | PrismaCertificationSchedulerSlot[] |  |

### PrismaChangelog (model, table: `changelogs`)

| Field | Type | Attributes |
|---|---|---|
| id | String | PK, default=uuid() |
| user_id | Int |  |
| action | ChangelogAction |  |
| table_name | String |  |
| ref_id | Int |  |
| ref_label | String? |  |
| created_at | DateTime | default=now() |
| items | PrismaChangelogItem[] |  |
| user | PrismaUser | relation |

### PrismaChangelogItem (model, table: `changelog_items`)

| Field | Type | Attributes |
|---|---|---|
| id | String | PK, default=uuid() |
| changelog_id | String |  |
| column_name | String |  |
| old_value | String? |  |
| new_value | String? |  |
| changelog | PrismaChangelog | relation |

### PrismaClientBlacklist (model, table: `client_blacklist`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| suppression_date | DateTime |  |
| suppression_until | DateTime |  |
| name | String? |  |
| last_name | String? |  |
| phone | String? |  |
| second_phone | String? |  |
| email | String? |  |
| identification_number | String? |  |
| reason | String? |  |
| client_id | Int |  |
| client | clients | relation |

### PrismaClientCalls (model, table: `client_calls`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| buyer_client_id | Int |  |
| seller_client_id | Int |  |
| interest_id | Int? |  |
| provider_metadata | Json? |  |
| status | client_call_status | default=INITIATED |
| started_at | DateTime? |  |
| ended_at | DateTime? |  |
| duration_seconds | Int? |  |
| webhook_received_at | DateTime? |  |
| recording_file_key | String? |  |
| transcription | String? |  |
| transcription_structured | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| buyer_client | clients | relation |
| seller_client | clients | relation |
| interest | PrismaInterest? | relation |

### PrismaClientCoOwner (model, table: `client_co_owners`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| client_id | Int | unique |
| name | String |  |
| last_name | String |  |
| second_last_name | String? |  |
| phone | String? |  |
| email | String? |  |
| identification_number | String? |  |
| identification_number_type | identification_number_type? |  |
| identification_valid_until | DateTime? |  |
| nationality | String? |  |
| residence_country | String? |  |
| country_of_birth | String? |  |
| date_birth | DateTime? |  |
| marital_status | String? |  |
| number_of_children | Int? |  |
| rent_or_mortgage_amount | Decimal? |  |
| loans_amount | Decimal? |  |
| card_amount | Decimal? |  |
| job_position | job_position_type? |  |
| monthly_income | Decimal? |  |
| professional_status | professional_status_type? |  |
| professional_activity | professional_activity_type? |  |
| seniority_date | DateTime? |  |
| career_start_date | DateTime? |  |
| permanent_contract | String? |  |
| company_name | String? |  |
| billing_address_id | Int? | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| client | clients | relation |
| billing_address | PrismaAddress? | relation |

### PrismaClientDocument (model, table: `client_documents`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| document_path | String |  |
| type | client_document_type |  |
| source | client_document_source? |  |
| client_id | Int |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deleted_at | DateTime? |  |
| client | clients | relation |

### PrismaConfiguration (model, table: `configurations`)

| Field | Type | Attributes |
|---|---|---|
| id | String | PK |
| value | Json |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |

### PrismaCustomer (model, table: `customers`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| ext_id | String? |  |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| email | String? |  |
| phone | String? |  |
| second_phone | String? |  |
| first_name | String? |  |
| middle_name | String? |  |
| first_surname | String? |  |
| second_surname | String? |  |
| birth_date | DateTime? |  |
| id_number | String? |  |
| id_type | identification_number_type? |  |
| company_id_number | String? |  |
| company_id_type | identification_number_type? |  |
| legal_nature | legal_nature_type? |  |
| legal_name | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| bank_accounts | PrismaBankAccount[] |  |
| addresses | PrismaAddress[] |  |

### PrismaDealCollectionsStatus (model, table: `deal_collections_statuses`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| deal_id | Int | unique |
| status | deal_collections_status_type |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| repurchased_date | DateTime? |  |
| recovered_date | DateTime? |  |
| reported_date | DateTime? |  |
| deals | deals | relation |

### PrismaDealNote (model, table: `deal_notes`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| deal_id | Int |  |
| author_id | Int? |  |
| ops_note_id | String? | unique |
| title | String |  |
| content | String |  |
| is_pinned | Boolean | default=false |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deal | deals | relation |
| author | PrismaUser? | relation |
| attachments | PrismaDealNoteAttachment[] |  |

### PrismaDealNoteAttachment (model, table: `deal_note_attachments`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| note_id | Int |  |
| location | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| note | PrismaDealNote | relation |

### PrismaDealStage (model, table: `deal_stages`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| deal_id | Int | unique |
| stage | stage_type |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deals | deals | relation |
| transitions | PrismaDealStageTransition[] |  |

### PrismaDealStageTransition (model, table: `deal_stage_transitions`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| deal_stage_id | Int |  |
| stage | stage_type |  |
| type | stage_transition_type? |  |
| started_at | DateTime | default=now() |
| finished_at | DateTime? |  |
| deal_stage | PrismaDealStage | relation |

### PrismaDealValuation (model, table: `deal_valuations`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| deal_id | Int | unique |
| insurance_fee_due_amount | Decimal? |  |
| operational_costs | Decimal? |  |
| raw_rent_due_amount | Decimal? |  |
| recieved_amount | Decimal? |  |
| rent_due_amount | Decimal? |  |
| risk_uw | Decimal? |  |
| taxes | Decimal? |  |
| total_amount_purchase | Decimal? |  |
| total_fee | Decimal? |  |
| rent_valuation | Decimal? |  |
| prime_valuation | Decimal? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| deal | deals | relation |

### PrismaDocumentAnalyses (model, table: `document_analyses`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| client_id | Int? |  |
| catalogue_vehicle_id | Int? |  |
| document_path | String |  |
| category | String |  |
| scope | String? |  |
| raw_data | Json |  |
| description | String? |  |
| updated_at | DateTime |  |
| created_at | DateTime | default=now() |
| client | clients? | relation |
| catalogue_vehicle | PrismaCatalogueVehicle? | relation |

### PrismaExternalVehicleProvider (model, table: `external_vehicle_providers`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | external_vehicle_provider_name | unique |
| associated_client_id | Int | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| associatedClient | clients | relation |
| catalogueVehicleExternalInfos | PrismaCatalogueVehicleExternalInfo[] |  |

### PrismaFinancialAggregationProducts (model, table: `financial_aggregation_products`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| aggregation_id | Int |  |
| product | String |  |
| type | financial_aggregation_product_type |  |
| is_owner | Boolean? |  |
| balance | Decimal |  |
| currency | currency |  |
| description | String? |  |
| transactions | PrismaFinancialAggregationTransactions[] |  |
| aggregation | PrismaFinancialAggregations | relation |

### PrismaFinancialAggregationTransactions (model, table: `financial_aggregation_transactions`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| product_id | Int |  |
| transaction_date | DateTime |  |
| value_date | DateTime? |  |
| amount | Decimal |  |
| balance | Decimal? |  |
| currency | currency |  |
| category | financial_aggregation_transaction_category |  |
| description | String? |  |
| product | PrismaFinancialAggregationProducts | relation |

### PrismaFinancialAggregations (model, table: `financial_aggregations`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| status | financial_aggregation_status_type | default=PENDING |
| received_at | DateTime? |  |
| identification_number | String? |  |
| identification_number_type | identification_number_type? |  |
| service | String? |  |
| deal_id | Int? |  |
| evaluated_at | DateTime? |  |
| result | String? |  |
| error | String? |  |
| deal | deals? | relation |
| products | PrismaFinancialAggregationProducts[] |  |

### PrismaFinancingRequest (model, table: `financing_requests`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| client_id | Int | unique |
| interest_id | Int? | unique |
| amount | Decimal |  |
| currency | currency | default=EUR |
| terms | Int |  |
| down_payment_amount | Decimal? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| client | clients | relation |
| interest | PrismaInterest? | relation |

### PrismaGatewayPayment (model, table: `gateway_payments`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| status | gateway_payment_status |  |
| amount | Decimal |  |
| currency | currency? |  |
| type | gateway_payment_type |  |
| product | String |  |
| gateway_provider | gateway_provider |  |
| gateway_identifier | String? | unique |
| gateway_response | Json? |  |
| reference_id | Int? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |

### PrismaInterest (model, table: `interests`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| acquisition_data | Json? |  |
| ad_price_amount | Decimal? |  |
| ad_price_currency | currency? |  |
| catalogue_vehicle_id | Int? |  |
| client_id | Int |  |
| commission_fee_amount | Decimal? |  |
| commission_fee_currency | currency? |  |
| delivery_expenses_amount | Decimal? |  |
| delivery_expenses_currency | currency? |  |
| discarded_at | DateTime? |  |
| discount_amount | Decimal? |  |
| discount_currency | currency? |  |
| external_payment_reference_id | String? |  |
| gpu_amount | Decimal? |  |
| gpu_currency | currency? |  |
| gpus_amount | Decimal? |  |
| gpus_currency | currency? |  |
| is_external | Boolean | default=false |
| is_main_interest | Boolean | default=false |
| metal_margin_amount | Decimal? |  |
| metal_margin_currency | currency? |  |
| operation_payment_method | operation_payment_method? |  |
| original_deal_id | Int? |  |
| origin_source | String? |  |
| premium_warranty_amount | Decimal? |  |
| premium_warranty_currency | currency? |  |
| premium_warranty_years | Int? |  |
| preparation_expenses_amount | Decimal? |  |
| preparation_expenses_currency | currency? |  |
| price_decrease_notification_sent | Boolean | default=false |
| product_source | String? |  |
| purchase_price_amount | Decimal? |  |
| purchase_price_currency | currency? |  |
| selected_financing_installments | Json? |  |
| selling_price_amount | Decimal? |  |
| selling_price_currency | currency? |  |
| sold_at | DateTime? |  |
| status | interest_status |  |
| substatus | interest_substatus |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| client | clients | relation |
| catalogue_vehicle | PrismaCatalogueVehicle? | relation |
| original_deal | deals? | relation |
| offers | PrismaOffer[] |  |
| submissions | PrismaSubmission[] |  |
| purchase_transactions | PrismaPurchaseTransactions[] |  |
| purchase_discounts | PrismaPurchaseDiscounts[] |  |
| reservation | PrismaReservation? |  |
| car_delivery | PrismaCarDeliveries? |  |
| interest_services | PrismaInterestService[] |  |
| client_calls | PrismaClientCalls[] |  |
| client_calls_normalized | ClientCallsNormalized[] |  |
| nps_submissions | PrismaNpsSubmission[] |  |
| certifications | PrismaCertification[] |  |
| financial_service | PrismaInterestFinancialService? |  |
| ai_voice_calls | PrismaAiVoiceCall[] |  |
| financing_request | PrismaFinancingRequest? |  |
| interest_ai | PrismaInterestAi? |  |

### PrismaInterestAi (model, table: `interests_ai`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| interest_id | Int | unique |
| reasons | String? |  |
| next_message_date | DateTime? |  |
| next_message_target | interest_ai_next_message_target? |  |
| contact_count | Int | default=0 |
| is_alert | Boolean | default=false |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| interest | PrismaInterest | relation |

### PrismaInterestFinancialService (model, table: `interest_financial_services`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| interest_id | Int | unique |
| financial_institution | financial_institution |  |
| financed_amount | Decimal |  |
| financed_amount_currency | currency |  |
| commission_amount | Decimal |  |
| commission_amount_currency | currency |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| interest | PrismaInterest | relation |

### PrismaInterestMetrics (view, table: `interest_metrics`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | unique |
| uuid | String | unique |
| license_plate | String? |  |
| total_discounts | Decimal? |  |
| ad_price | Decimal? |  |
| purchase_price | Decimal? |  |
| preparation_expenses | Decimal? |  |
| delivery_expenses | Decimal? |  |
| premium_warranty | Decimal? |  |
| commission_fee_amount | Decimal? |  |
| gpu | Decimal? |  |
| gpus | Decimal? |  |
| metal_margin | Decimal? |  |
| total_selling_price | Decimal? |  |
| reservation_amount | Decimal? |  |
| total_financed | Decimal? |  |
| total_transactions | Decimal? |  |
| total_revenues | Decimal? |  |

### PrismaInterestService (model, table: `interest_services`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| interest_id | Int |  |
| service_id | Int |  |
| price_amount | Decimal |  |
| price_currency | currency |  |
| is_paid | Boolean | default=false |
| created_at | DateTime | default=now() |
| interest | PrismaInterest | relation |
| service | PrismaService | relation |

### PrismaMultipublisherError (model, table: `multipublisher_errors`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| catalogue_vehicle_id | Int |  |
| type | String |  |
| publisher | String |  |
| reason | String |  |
| message | String |  |
| created_at | DateTime | default=now() |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |

### PrismaNote (model, table: `notes`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| client_id | Int? |  |
| ref_id | Int? |  |
| ref_type | ref_note_type |  |
| title | String |  |
| content | String |  |
| is_pinned | Boolean | default=false |
| author_id | Int? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| author | PrismaUser? | relation |
| catalogue_vehicle | PrismaCatalogueVehicle? | relation |
| client | clients? | relation |
| attachments | PrismaNoteAttachment[] |  |

### PrismaNoteAttachment (model, table: `note_attachments`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| note_id | Int |  |
| location | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| note | PrismaNote | relation |

### PrismaNpsForm (model, table: `nps_forms`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| name | String |  |
| fields_schema | Json |  |
| template_name | String |  |
| template_workspace | String |  |
| template_vars | Json | default="{}" |
| is_active | Boolean | default=true |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| submissions | PrismaNpsSubmission[] |  |

### PrismaNpsSubmission (model, table: `nps_submissions`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| form_id | Int |  |
| public_id | String | unique |
| client_id | Int |  |
| interest_id | Int? |  |
| ext_id | String? |  |
| link_opened_at | DateTime? |  |
| submitted_at | DateTime? |  |
| answered_at | DateTime? |  |
| nps_probability | Int? |  |
| answers | Json? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| form | PrismaNpsForm | relation |
| client | clients | relation |
| interest | PrismaInterest? | relation |
| catalogue_vehicle | PrismaCatalogueVehicle? | relation |

### PrismaOAuthPkceSession (model, table: `oauth_pkce_sessions`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| provider | String |  |
| state | String | unique |
| code_verifier | String |  |
| expires_at | DateTime |  |
| created_at | DateTime | default=now() |

### PrismaOAuthToken (model, table: `oauth_tokens`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| provider | String | unique |
| encrypted_access_token | String |  |
| encrypted_refresh_token | String |  |
| access_token_expires_at | DateTime |  |
| refresh_token_expires_at | DateTime |  |
| token_type | String | default="Bearer" |
| scope | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |

### PrismaOffer (model, table: `offers`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| deal_id | Int? |  |
| interest_id | Int? |  |
| status | offer_status_type |  |
| asked_amount | Decimal |  |
| asked_currency | currency |  |
| loan_amount | Decimal |  |
| loan_currency | currency |  |
| terms | Int |  |
| nir | Decimal |  |
| apr | Decimal |  |
| monthly_fee_amount | Decimal |  |
| monthly_fee_currency | currency |  |
| insurance_fee_amount | Decimal |  |
| insurance_fee_currency | currency |  |
| insurance_type | insurance_types? |  |
| commission_fee_amount | Decimal |  |
| commission_fee_currency | currency |  |
| commission_fee_rate | Decimal | default=0 |
| admin_fee_amount | Decimal |  |
| admin_fee_currency | currency |  |
| loan_total_cost_amount | Decimal? |  |
| loan_total_cost_currency | currency? |  |
| financier | String |  |
| is_selected | Boolean | default=false |
| selected_at | DateTime? |  |
| not_allowed_reason | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deal | deals? | relation |
| submission | PrismaSubmission? |  |
| interest | PrismaInterest? | relation |

### PrismaPaymentBreakdowns (model, table: `payment_breakdowns`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| purchase_date | DateTime |  |
| income_type | payment_income_type |  |
| amount | Decimal |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicle_id | Int |  |
| author_id | Int |  |
| catalogue_vehicle | PrismaCatalogueVehicle | relation |
| author | PrismaUser | relation |

### PrismaPreoffer (model, table: `preoffers`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| deal_id | Int | unique |
| license_plate | String |  |
| pvp_ask_amount | Decimal? |  |
| pvp_ask_currency | currency? |  |
| commission_amount | Decimal? |  |
| commission_currency | currency? |  |
| pvp_amount | Decimal? |  |
| pvp_currency | currency? |  |
| monthly_income_amount | Decimal? |  |
| monthly_income_currency | currency? |  |
| pvp_max_amount | Decimal? |  |
| pvp_max_currency | currency? |  |
| ganvam_amount | Decimal? |  |
| ganvam_currency | currency? |  |
| motor_es_amount | Decimal? |  |
| motor_es_currency | currency? |  |
| bca_amount | Decimal? |  |
| bca_currency | currency? |  |
| car_matrix_amount | Decimal? |  |
| car_matrix_currency | currency? |  |
| error | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| deal | deals | relation |
| preoffer_proposals | PrismaPreofferProposal[] |  |

### PrismaPreofferProposal (model, table: `preoffer_proposals`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| preoffer_id | Int |  |
| term | Int |  |
| tae | Decimal |  |
| tin | Decimal |  |
| due_amount | Decimal |  |
| due_currency | currency |  |
| total_amount | Decimal |  |
| total_currency | currency |  |
| total_cost_credit_amount | Decimal |  |
| total_cost_credit_currency | currency |  |
| total_interest_amount | Decimal |  |
| total_interest_currency | currency |  |
| is_selected | Boolean | default=false |
| created_at | DateTime | default=now() |
| preoffer | PrismaPreoffer | relation |

### PrismaProvince (model, table: `provinces`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | String | unique |
| slug | String | unique |
| code | String | unique |
| coordinates | Unsupported |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| zip_code_prefix | String? |  |
| catalogue_vehicles | PrismaCatalogueVehicle[] |  |
| catalogue_vehicle_client_history | PrismaCatalogueVehicleClientHistory[] |  |
| clients | clients[] |  |
| province_equivalences | PrismaProvinceEquivalence[] |  |

### PrismaProvinceEquivalence (model, table: `province_equivalences`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| alias_name | String | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| province_id | Int |  |
| province | PrismaProvince | relation |

### PrismaPuntoAi (model, table: `punto_ai`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| cache_identifier | String | unique |
| request | Json |  |
| response | Json |  |
| tax_amount | Decimal? |  |
| tax_result | String? |  |
| status | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| expires_at | DateTime |  |

### PrismaPurchaseDiscounts (model, table: `purchase_discounts`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deal_id | Int? |  |
| interest_id | Int? |  |
| concept | String |  |
| amount | Decimal |  |
| currency | currency |  |
| deal | deals? | relation |
| interest | PrismaInterest? | relation |

### PrismaPurchaseTransactions (model, table: `purchase_transactions`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deal_id | Int? |  |
| interest_id | Int? |  |
| date | DateTime |  |
| method | purchase_transaction_method_type |  |
| amount | Decimal |  |
| currency | currency |  |
| collected_at | DateTime? |  |
| deleted_at | DateTime? |  |
| trade_in_vehicle_id | Int? | unique |
| deal_transfer_link | String? |  |
| deal | deals? | relation |
| trade_in_vehicle | PrismaCatalogueVehicle? | relation |
| interest | PrismaInterest? | relation |

### PrismaRequestLogs (model, table: `request_logs`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| created_at | DateTime | default=now() |
| method | String |  |
| url | String |  |
| req_body | Json? |  |
| req_headers | Json |  |
| res_status | Int |  |
| res_body | Json? |  |

### PrismaReservation (model, table: `reservations`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| deal_id | Int? | unique |
| interest_id | Int? | unique |
| reservation_date | DateTime |  |
| returned_date | DateTime? |  |
| discarded_no_refund_date | DateTime? |  |
| amount | Decimal |  |
| currency | currency |  |
| status | reservation_status_type |  |
| method | reservation_method_type |  |
| cancel_reason | reservation_cancel_reason_type? |  |
| change_of_client_name | String? |  |
| change_of_client_phone | String? |  |
| deal | deals? | relation |
| interest | PrismaInterest? | relation |

### PrismaRespondioAssignees (model, table: `respondio_assignees`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| ext_assignee_id | String | unique |
| first_name | String? |  |
| last_name | String? |  |
| email | String |  |
| contacts | PrismaRespondioContacts[] |  |

### PrismaRespondioAttachments (model, table: `respondio_attachments`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| message_id | Int |  |
| type | respondio_attachment_type |  |
| url | String |  |
| file_name | String |  |
| ext | String |  |
| size | Int |  |
| mime | String |  |
| message | PrismaRespondioMessages | relation |

### PrismaRespondioContacts (model, table: `respondio_contacts`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| ext_contact_id | String | unique |
| assignee_id | Int? |  |
| first_name | String? |  |
| last_name | String? |  |
| phone | String |  |
| email | String? |  |
| language | String? |  |
| profile_pic | String? |  |
| country_code | String? |  |
| tags | String[] |  |
| workspace | respondio_workspace? |  |
| assignee | PrismaRespondioAssignees? | relation |
| messages | PrismaRespondioMessages[] |  |
| tag_events | PrismaRespondioTagEvents[] |  |

### PrismaRespondioMessages (model, table: `respondio_messages`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| contact_id | Int |  |
| timestamp | DateTime |  |
| traffic | respondio_message_traffic |  |
| type | respondio_message_type |  |
| text | String? |  |
| contact | PrismaRespondioContacts | relation |
| attachments | PrismaRespondioAttachments[] |  |

### PrismaRespondioTagEvents (model, table: `respondio_tag_events`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| created_at | DateTime | default=now() |
| contact_id | Int |  |
| action | respondio_tag_event_action |  |
| tag | String |  |
| contact | PrismaRespondioContacts | relation |

### PrismaService (model, table: `services`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| type | service_type |  |
| scope | service_scope |  |
| name | service_name |  |
| price_amount | Decimal |  |
| price_currency | currency |  |
| payment_link | String? |  |
| translations | Json? |  |
| disabled_at | DateTime? |  |
| created_at | DateTime | default=now() |
| interest_services | PrismaInterestService[] |  |
| catalogue_vehicle_services | PrismaCatalogueVehicleService[] |  |

### PrismaSubmission (model, table: `submissions`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| financier_id | String? | unique |
| financier_code | String? | unique |
| deal_id | Int? |  |
| interest_id | Int? |  |
| offer_id | Int | unique |
| main_status | submission_main_status_type | default=PENDING |
| sub_status | submission_sub_status_type? |  |
| financier_status | String? |  |
| documents_needed | loan_document_type[] |  |
| asked_amount | Decimal |  |
| asked_currency | currency |  |
| loan_amount | Decimal |  |
| loan_currency | currency |  |
| terms | Int |  |
| nir | Decimal |  |
| apr | Decimal |  |
| down_payment_amount | Decimal? |  |
| down_payment_currency | currency? |  |
| commitment_fee_amount | Decimal? |  |
| commitment_fee_currency | currency? |  |
| monthly_fee_amount | Decimal |  |
| monthly_fee_currency | currency |  |
| life_insurance_fee_amount | Decimal |  |
| life_insurance_fee_currency | currency |  |
| insurance_type | insurance_types? |  |
| commission_fee_amount | Decimal |  |
| commission_fee_currency | currency |  |
| commission_fee_rate | Decimal | default=0 |
| admin_fee_amount | Decimal |  |
| admin_fee_currency | currency |  |
| loan_total_cost_amount | Decimal? |  |
| loan_total_cost_currency | currency? |  |
| financier | String |  |
| status_transitions | PrismaSubmissionStatusTransitions[] |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| early_termination | DateTime? |  |
| refunded_financial_commission | Decimal? |  |
| refunded_financial_commission_currency | currency? |  |
| is_loan | Boolean | default=false |
| use_co_owner | Boolean | default=false |
| finance_user_id | Int? |  |
| num_revisions | Int? |  |
| deal | deals? | relation |
| offer | PrismaOffer | relation |
| interest | PrismaInterest? | relation |
| finance_user | PrismaUser? | relation |
| submission_documents | PrismaSubmissionDocument[] |  |

### PrismaSubmissionDocument (model, table: `submission_documents`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| submission_id | Int |  |
| document_type | loan_document_type |  |
| status | loan_document_status_type |  |
| external_document_id | String? |  |
| error_detail | String? |  |
| created_at | DateTime | default=now() |
| submission | PrismaSubmission | relation |

### PrismaSubmissionStatusTransitions (model, table: `submission_status_transitions`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| submission_id | Int |  |
| current_main_status | submission_main_status_type |  |
| previous_main_status | submission_main_status_type? |  |
| current_sub_status | submission_sub_status_type? |  |
| previous_sub_status | submission_sub_status_type? |  |
| author_id | Int? |  |
| created_at | DateTime | default=now() |
| reason | String? |  |
| started_at | DateTime? | default=now() |
| finished_at | DateTime? |  |
| author | PrismaUser? | relation |
| submission | PrismaSubmission | relation |

### PrismaUser (model, table: `users`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| external_id | String | unique |
| email | String | unique |
| given_name | String |  |
| family_name | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| ops_user_id | String? | unique |
| roles | user_roles[] | default=[] |
| is_deleted | Boolean | default=false |
| sales_deals | deals[] | relation |
| finance_deals | deals[] | relation |
| finance_submissions | PrismaSubmission[] | relation |
| certifier_deals | deals[] | relation |
| notes | PrismaDealNote[] |  |
| catalogue_vehicle_inspections | PrismaCatalogueVehicleInspection[] |  |
| PrismaSubmissionStatusTransition | PrismaSubmissionStatusTransitions[] |  |
| PrismaCatalogueVehiclesStatusTransitions | PrismaCatalogueVehiclesStatusTransitions[] |  |
| generic_note | PrismaNote[] |  |
| PrismaCatalogueVehiclesRepricing | PrismaCatalogueVehiclesRepricing[] |  |
| processor_user | PrismaCatalogueVehicle[] | relation |
| catalogue_vehicle_client_history | PrismaCatalogueVehicleClientHistory[] | relation |
| credentials | credentials[] |  |
| payment_breakdowns | PrismaPaymentBreakdowns[] |  |
| changelogs | PrismaChangelog[] |  |
| clients | clients[] | relation |
| certifications | PrismaCertification[] | relation |
| cancelled_certifications | PrismaCertification[] | relation |
| scheduler_slots | PrismaCertificationSchedulerSlot[] | relation |

### PrismaVehicle (model, table: `vehicles`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| license_plate | String | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| brand | String? |  |
| model | String? |  |
| version | String? |  |
| vehicle_color_id | Int? |  |
| year_registration | Int? |  |
| engine_power_hp | Decimal? |  |
| vin | String? |  |
| alert_stolen | Boolean? |  |
| max_legal_owners | Boolean? |  |
| legal_owners_size | Int? |  |
| alert_leasing | Boolean? |  |
| alert_damage | Boolean? |  |
| alert_km | Boolean? |  |
| alert_rental | Boolean? |  |
| alert_imported | Boolean? |  |
| last_inspection_failed | Boolean? |  |
| alert_province | Boolean? |  |
| gear_type | String? |  |
| fuel_type | String? |  |
| gearbox_type | gearbox_type? |  |
| combustible_type | combustible_type? |  |
| last_odometer_reading_value | Decimal? |  |
| first_registration_date | DateTime? |  |
| deals | deals[] |  |
| rejections | String[] | default=[] |
| last_owner_change_date | DateTime? |  |
| last_stolen_date | DateTime? |  |
| transferable | transferable_vehicle? |  |
| title_reservation | Boolean? |  |
| has_debt | Boolean? |  |
| province | String? |  |
| vehicle_inspection_passed | Boolean? |  |
| valid_vehicle_inspection | Boolean? |  |
| next_vehicle_inspection_date | DateTime? |  |
| vehicle_color | PrismaVehicleColor? | relation |

### PrismaVehicleColor (model, table: `vehicle_colors`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | String | unique |
| slug | String | unique |
| sumauto_id | Int? | unique |
| cochesnet_id | Int? | unique |
| wallapop_id | String? | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| catalogue_vehicles | PrismaCatalogueVehicle[] |  |
| PrismaVehicle | PrismaVehicle[] |  |
| catalogue_vehicle_client_history | PrismaCatalogueVehicleClientHistory[] |  |

### PrismaVehicleMake (model, table: `vehicle_makes`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| sumauto_id | Int? |  |
| models | PrismaVehicleModel[] |  |
| catalogue_vehicles | PrismaCatalogueVehicle[] |  |
| carfax_equivalences | PrismaCarfaxVehicleEquivalence[] |  |

### PrismaVehicleModel (model, table: `vehicle_models`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| vehicle_make_id | Int |  |
| sumauto_id | Int? |  |
| make | PrismaVehicleMake | relation |
| versions | PrismaVehicleVersion[] |  |
| catalogue_vehicles | PrismaCatalogueVehicle[] |  |
| carfax_equivalences | PrismaCarfaxVehicleEquivalence[] |  |

### PrismaVehicleVersion (model, table: `vehicle_versions`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| vehicle_model_id | Int |  |
| model | PrismaVehicleModel | relation |
| years | PrismaVehicleYear[] | relation |
| catalogue_vehicles | PrismaCatalogueVehicle[] |  |

### PrismaVehicleYear (model, table: `vehicle_years`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| value | Int | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime |  |
| versions | PrismaVehicleVersion[] | relation |
| catalogue_vehicles | PrismaCatalogueVehicle[] |  |

### appraisals (model, table: `appraisals`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| license_plate | String |  |
| kilometers | Int |  |
| make | String |  |
| mech_grade | String |  |
| body_grade | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| expires_at | DateTime |  |
| data | Json |  |
| status_code | Int | default=200 |

### asnef_equifax (model, table: `asnef_equifax`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| identification_number | String |  |
| number_of_operations | Decimal? |  |
| total_amount_of_operations | Decimal? |  |
| number_of_unpaid_operations | Decimal? |  |
| number_of_unpaid_payments | Decimal? |  |
| total_unpaid_payment_amount | Decimal? |  |
| maximum_unpaid_payment_amount | Decimal? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| expired_at | DateTime |  |
| raw_data | Json? |  |
| errors | Json? |  |

### carfax (model, table: `carfax`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| vehicle_identifier | String | unique |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| expires_at | DateTime |  |
| data | Json? |  |
| status | carfax_service_status | default=SUCCESS |
| error | String? |  |
| retries | Int | default=0 |

### clients (model, table: `clients`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| name | String |  |
| last_name | String |  |
| second_last_name | String? |  |
| phone | String? |  |
| second_phone | String? |  |
| email | String? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| promo_code | String? |  |
| acquisition_data | Json? |  |
| referral_code | String? | default=dbgenerated("generate_random_code(6)") |
| ops_client_id | String? | unique |
| identification_number | String? |  |
| identification_number_type | identification_number_type? |  |
| identification_valid_until | DateTime? |  |
| fiscal_identification_number | String? |  |
| fiscal_identification_number_type | identification_number_type? |  |
| nationality | String? |  |
| date_birth | DateTime? |  |
| preferred_contact_methods | String[] | default=[] |
| preferred_contact_times | String[] | default=[] |
| is_terms_and_condition_accepted | Boolean? |  |
| job_position | job_position_type? |  |
| marital_status | String? |  |
| monthly_income | Decimal? |  |
| annual_income | Decimal? |  |
| company_name | String? |  |
| professional_status | professional_status_type? |  |
| professional_activity | professional_activity_type? |  |
| seniority_date | DateTime? |  |
| career_start_date | DateTime? |  |
| last_date_payroll | DateTime? |  |
| income_source | String? |  |
| permanent_contract | String? |  |
| job_type | String? |  |
| company_billing_type | String? |  |
| is_delinquency_approved | Boolean? |  |
| residence_start_date | DateTime? |  |
| country_of_birth | String? |  |
| residence_card_expiration_date | DateTime? |  |
| social_security_registration_date | DateTime? |  |
| number_of_jobs | Int? |  |
| gender | gender? |  |
| number_of_children | Int? |  |
| rent_or_mortgage_amount | Decimal? |  |
| loans_amount | Decimal? |  |
| card_amount | Decimal? |  |
| cirbe_source | String? |  |
| iban | String? |  |
| swift | String? |  |
| is_account_at_least_6_months_older | Boolean | default=false |
| is_balance_at_least_200 | Boolean | default=false |
| has_microloans | Boolean? |  |
| legal_nature | legal_nature_type? |  |
| legal_name | String? |  |
| residence_country | String? |  |
| ext_id | String? |  |
| external_ids | Json | default="{}" |
| link_doc_folder | String? |  |
| is_deleted | Boolean | default=false |
| billing_address_id | Int? |  |
| sales_agent_id | Int? |  |
| sales_agent_assigned_at | DateTime? |  |
| registration_province_id | Int? |  |
| deals | deals[] |  |
| billing_address | PrismaAddress? | relation |
| registration_province | PrismaProvince? | relation |
| black_listed_clients | PrismaClientBlacklist[] |  |
| catalogue_vehicles | PrismaCatalogueVehicle[] | relation |
| catalogue_vehicle_client_history | PrismaCatalogueVehicleClientHistory[] |  |
| prismaExternalVehicleProvider | PrismaExternalVehicleProvider? |  |
| interests | PrismaInterest[] |  |
| sales_agent | PrismaUser? | relation |
| notes | PrismaNote[] | relation |
| documents | PrismaClientDocument[] |  |
| buyer_calls | PrismaClientCalls[] | relation |
| seller_calls | PrismaClientCalls[] | relation |
| buyer_calls_normalized | ClientCallsNormalized[] | relation |
| seller_calls_normalized | ClientCallsNormalized[] | relation |
| appraisals_trade_in | PrismaAppraisalTradeIn[] |  |
| nps_submissions | PrismaNpsSubmission[] |  |
| certifications | PrismaCertification[] | relation |
| co_owner | PrismaClientCoOwner? |  |
| document_analyses | PrismaDocumentAnalyses[] |  |
| financing_request | PrismaFinancingRequest? |  |

### credentials (model, table: `credentials`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| prefix | String | unique |
| hash_key | String |  |
| scopes | String[] |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| affiliate_id | Int? |  |
| user_id | Int? |  |
| affiliate | PrismaAffiliate? | relation |
| user | PrismaUser? | relation |

### deal_stages_updates (model, table: `deal_stages_updates`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| deal_id | Int |  |
| ops_stage_id | String |  |
| started_at | DateTime | default=now() |
| finished_at | DateTime? |  |
| deals | deals | relation |

### deals (model, table: `deals`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| client_id | Int |  |
| vehicle_id | Int? |  |
| catalogue_vehicle_id | Int? |  |
| affiliate_id | Int? |  |
| sales_user_id | Int? |  |
| finance_user_id | Int? |  |
| certifier_user_id | Int? |  |
| interest_id | Int? |  |
| payment_day | Int? |  |
| ask | Decimal? |  |
| link_doc_folder | String? |  |
| lost_reason | String? |  |
| ops_deal_id | String? | unique |
| ops_owner_name | String? |  |
| ops_stage_id | String? |  |
| product_source | String? |  |
| product_source_client_id | String? |  |
| product_funnel | String? |  |
| reopened_at | DateTime? |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| first_won_time | DateTime? |  |
| lost_time | DateTime? |  |
| origin_source | origin_source_type? |  |
| situation | deal_situation_type? |  |
| status | deal_status_type? |  |
| loan_installment | Decimal? |  |
| loan_unpaid | Decimal? |  |
| loan_pending_installments | Int? |  |
| original_financial | String? |  |
| product_type | String? |  |
| loan_entry | Decimal? |  |
| total_original_loan_amount | Decimal? |  |
| total_original_loan_installments | Int? |  |
| new_loan_amount | Decimal? |  |
| new_loan_installments | Int? |  |
| original_loan_interest_rate | Decimal? |  |
| new_loan_interest_rate | Decimal? |  |
| new_loan_insurances | String[] | default=[] |
| new_loan_installment | Decimal? |  |
| new_loan_tin | Decimal? |  |
| is_financed | Boolean? |  |
| bank_fee | Decimal? |  |
| etpf | String? |  |
| rejections | String[] | default=[] |
| max_financing_period | Int? |  |
| duplicate_fields | String[] | default=[] |
| duplicate_deal_id | Int? |  |
| eligible_financiers | Json? |  |
| eligible_financier_names | String[] | default=[] |
| eligible_financier_rejections | String[] | default=[] |
| eligible_rent_rejections | String[] | default=[] |
| no_eligible_financier_reasons | Json | default="{}" |
| financial_aggregation_result | String? |  |
| selected_financier | String? |  |
| ops_update_date | DateTime? |  |
| acquisition_data | Json? |  |
| selected_financing_installments | Json? |  |
| loan_purpose | loan_purpose_type? |  |
| tier | deal_tier_type? |  |
| clients | clients | relation |
| vehicles | PrismaVehicle? | relation |
| catalogue_vehicle | PrismaCatalogueVehicle? | relation |
| affiliate | PrismaAffiliate? | relation |
| sales_user | PrismaUser? | relation |
| finance_user | PrismaUser? | relation |
| certifier_user | PrismaUser? | relation |
| deal_stages_updates | deal_stages_updates[] |  |
| installments | installments[] |  |
| preoffer | PrismaPreoffer? |  |
| offers | PrismaOffer[] |  |
| submissions | PrismaSubmission[] |  |
| deal_valuations | PrismaDealValuation? |  |
| stage | PrismaDealStage? |  |
| collections_status | PrismaDealCollectionsStatus? |  |
| notes | PrismaDealNote[] |  |
| affiliate_campaign_cost | PrismaAffiliateCampaignCosts? |  |
| financial_aggregations | PrismaFinancialAggregations[] |  |
| preparation_expenses_amount | Decimal? |  |
| preparation_expenses_currency | currency? |  |
| delivery_expenses_amount | Decimal? |  |
| delivery_expenses_currency | currency? |  |
| premium_warranty_amount | Decimal? |  |
| premium_warranty_currency | currency? |  |
| premium_warranty_years | Int? |  |
| has_second_key | Boolean? |  |
| gps_uninstallation_date_time | DateTime? |  |
| gps_installation_date_time | DateTime? |  |
| take_insurance_date_time | DateTime? |  |
| cancel_insurance_date_time | DateTime? |  |
| reservation | PrismaReservation? |  |
| car_delivery | PrismaCarDeliveries? |  |
| purchase_transactions | PrismaPurchaseTransactions[] |  |
| purchase_discounts | PrismaPurchaseDiscounts[] |  |
| is_starred | Boolean | default=false |
| price_decrease_notification_sent | Boolean | default=false |
| external_payment_reference_id | String? |  |
| interest | PrismaInterest? |  |

### ganvam (model, table: `ganvam`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| trimester | String |  |
| make | String |  |
| model | String |  |
| fuel | String |  |
| year | Int |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| expires_at | DateTime |  |
| data | Json |  |

### installments (model, table: `installments`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| deal_id | Int |  |
| amount | Decimal |  |
| paid_amount | Decimal |  |
| penalty_amount | Decimal |  |
| due_date | DateTime |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| status | installment_status_type |  |
| deals | deals | relation |
| tax_base | Decimal |  |
| invoices | invoices[] |  |
| payment_plans | payment_plans[] |  |

### invoices (model, table: `invoices`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| installment_id | Int |  |
| amount | Decimal |  |
| due_date | DateTime |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| status | invoice_status_type |  |
| installments | installments | relation |
| payments | payments[] |  |

### motor_es (model, table: `motor_es`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| link | String |  |
| price | Int |  |
| fund_price | String |  |
| make | String |  |
| model | String |  |
| version | String |  |
| fuel | String |  |
| cv | Int |  |
| km | Int |  |
| bodywork | String |  |
| registration | String |  |
| guarantee | String |  |
| gear | String |  |
| seats | String |  |
| doors | String |  |
| color_exterior | String |  |
| color_interior | String |  |
| dealer_url | String |  |
| year | Int |  |
| complete_name | String |  |
| merchant_name | String |  |
| city | String |  |
| province | String |  |
| merchant_slug | String |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |

### motor_es_makes (model, table: `motor_es_makes`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| make | String |  |
| models | motor_es_models[] |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |

### motor_es_models (model, table: `motor_es_models`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| model | String |  |
| make_id | Int |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| motor_es_makes | motor_es_makes | relation |

### motor_es_years (model, table: `motor_es_years`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| year | Int |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |

### payment_plans (model, table: `payment_plans`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| installment_id | Int |  |
| initial_amount | Decimal |  |
| delayed_amount | Decimal |  |
| date | DateTime |  |
| due_date | DateTime |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| installments | installments | relation |

### payments (model, table: `payments`)

| Field | Type | Attributes |
|---|---|---|
| id | Int | PK, default=autoincrement() |
| uuid | String | unique, default=dbgenerated("gen_random_uuid()") |
| invoice_id | Int |  |
| method | String |  |
| remarks | String? |  |
| amount | Decimal |  |
| date | DateTime |  |
| created_at | DateTime | default=now() |
| updated_at | DateTime | default=now() |
| invoices | invoices | relation |

## Enums

- **ChangelogAction**: CREATE, UPDATE, DELETE
- **affiliate_bidding_type**: CPA, CPL, CPC
- **ai_voice_call_data_storage_setting**: EVERYTHING, EVERYTHING_EXCEPT_PII, BASIC_ATTRIBUTES_ONLY
- **ai_voice_call_direction**: INBOUND, OUTBOUND
- **ai_voice_call_sentiment**: POSITIVE, NEGATIVE, NEUTRAL, UNKNOWN
- **ai_voice_call_status**: ENDED, ERROR
- **ai_voice_call_type**: PHONE_CALL, WEB_CALL
- **belender_document_type**: CIRBE
- **bodywork_type**: SEDAN, CONVERTIBLE, COUPE, WAGON, VAN, MPV, SUV, HATCHBACK, PICKUP, COMPACT
- **capacity_unit**: LITERS, KWH
- **carfax_service_status**: SUCCESS, PENDING, ERROR
- **catalogue_vehicle_ad_source_type**: COCHESNET, AUTOCASION, AUTOSCOUT // @deprecated same as AUTOCASION, MILANUNCIOS, WALLAPOP, DEALER, COCHESCOM, CLIDRIVECOM, SUMAUTO, ARVAL, BANSACAR, AUTOPOMO, AYVENS
- **catalogue_vehicle_business_type**: B2B2B, C2B2B, C2B2C, B2B2C
- **catalogue_vehicle_document_type**: FILE, IMAGE, REPORT, DAMAGE_IMAGE
- **catalogue_vehicle_image_source**: MAXTERAUTO, C2C_S3, UNKNOWN
- **catalogue_vehicle_jato_data_type**: TECHNICAL, EXTERIOR, INTERIOR, MULTIMEDIA, CONFORT, SECURITY
- **catalogue_vehicle_notification_type**: REPRICING, P2M_REPRICING, AVAILABILITY, HIGH_INTEREST
- **catalogue_vehicles_status_type**: NEW, NOT_ELIGIBLE, CONTACTED, APPROVED, PUBLISHED, BOUGHT, UNPUBLISHED, DISCARDED
- **catalogue_vehicles_sub_status_type**: PENDING_APPRAISAL, PENDING_CONTACTED_APPRAISAL, NO_ADVERTISEMENT, NO_PHONE, NO_MINIMUM_INFORMATION, DUPLICATE, OUTSIDE_CRITERIA, OUT_OF_PRICE, LOW_PRICE, PENDING_CONTACT, CONTACTED_BY_PHONE, CONTACTED_BY_WHATSAPP, IN_PROCESS, PENDING_DOCUMENTATION, PHOTO_ISSUE, PENDING_VERSION, PENDING_IMPORT_EXTRAS, EXTRAS_ISSUE, PENDING_EXTERNAL_SHEET, PENDING_PUBLICATION, PUBLISHED_STOCK, PUBLISHED_STOCK_PRECERTIFIED, PUBLISHED_STOCK_CERTIFIED, OWNED_CLIDRIVE, PRICE_DISAGREEMENT, NOT_INTERESTED, NOT_AVAILABLE, NO_RESPONSE, SOLD, SOLD_BY_OWNER, OWNER_NOT_SELLING, OWNER_CANNOT_SELL, PROPOSED_REPRICING, REPRICING_ACCEPTED, REPRICING_DENIED, REPRICING_SENT, SENT_TO_BOT, DOCUMENTATION_RECEIVED, PENDING_PHOTO_EDITING, VEHICLE_NOT_ELIGIBLE, PHOTO_EDITING_KO, MILEAGE_TAMPERED, CAR_WITH_DAMAGE, CAR_WITH_MODIFICATIONS, OUT_OF_CRITERIA, CARFAX_ALERT, MANAGED_BY_CLIDRIVE, REQUIRES_PHONE_CALL
- **certification_status**: SCHEDULED, CANCELLED, COMPLETED
- **client_call_status**: INITIATED, IN_PROGRESS, HANGUP, COMPLETED, FAILED, DUPLICATED
- **client_document_source**: CLIENT_DOC, CLIDRIVE_DOC
- **client_document_type**: PDF_FILE, IMAGE
- **combustible_type**: GASOLINE, DIESEL, ELECTRIC, HYBRID_DIESEL, HYBRID_GASOLINE, MICROHYBRID_DIESEL, MICROHYBRID_GASOLINE, GASOLINE_LPG, GASOLINE_CNG, PLUG_IN_HYBRID
- **consumption_unit**: LITERS_PER_100_KM, KWH_PER_100_KM
- **currency**: EUR, USD
- **deal_collections_status_type**: ONGOING, DELAYED, SOLD, REPURCHASED, REPORTABLE, REPORTED, RECOVERED
- **deal_situation_type**: OPEN, WON, LOST, DELETED
- **deal_status_type**: SALES, DISCARDED, REJECTED
- **deal_tier_type**: RENT, PAID, FINANCED, C2C, DEALER
- **delivery_cleaning_status**: NOT_CLEANED, CLEANING, CLEAN
- **delivery_provider_type**: INHOUSE_TRANSPORT, LPS, WEDELIVERY, DRIIVEME, PYRAMID
- **delivery_requested_doc_status**: NOT_REQUESTED, REQUESTED, RECEIVED
- **delivery_sent_doc_status**: PENDING, SENT
- **delivery_signed_doc_status**: PENDING, SENT, SIGNED
- **drivetrain_type**: FRONT_WHEEL, REAR_WHEEL, FOUR_WHEEL
- **energy_classification_type**: ZERO, ECO, C, B, NO_BADGE
- **external_vehicle_provider_name**: ARVAL, BANSACAR, AYVENS, AUTOPOMO
- **financial_aggregation_product_type**: CHECKING, CARD, DEBIT, LINEOFCREDIT, SAVING, LOAN, INSURANCE, INVESTMENT, SECURITIES, PENSIONPLAN, DEPOSIT, CONFIRMING, FACTORING, GUARANTEE, LEASING, TPV, RISK, REMITTANCES, STOCKS, DISCOUNT, MORTGAGE, PERSONALINFORMATION, OTHER
- **financial_aggregation_status_type**: PENDING, CLIENT_ERROR, INVALID_DATA_RECEIVED, DATA_RECEIVED, EVALUATION_ERROR, EVALUATED
- **financial_aggregation_transaction_category**: UNCLASSIFIED, FUEL, PHONE_INTERNET, GROCERIES, UTILITIES, ATM_TRANSACTION, FEES, CASH_DEPOSIT, LOAN_RETURN, PAYROLL, TAXES, INTERESTS, ONLINE_SHOPPING, INSURANCES, PENSION_PLAN, EDUCATION, TRANSPORTATION, HEALTH, BILL_PAYMENT, TRANSFERS, TELEVISION, STORES, NGO, INVESTMENT_PRODUCTS, COMMUNITY_RENT, HAIR_SALON, PET, RESTAURANTS_BARS, CREDIT_CARD, HOTEL, CAPITAL_INCREASE, DIVIDEND_COLLECTION, DEPOSIT_FEE, BROKERAGE_COMMISSION, RIGHTS_PURCHASE, BUY_SELL_STOCKS, STOCK_DIVIDEND, PREMIUM, FUND_REFUND, FUND_SUBSCRIPTIONS, RIGHTS_SALE, PAYMENT_TERMINAL, GAMBLING_BETTING_CASINOS, MICROLOANS, EFC, SEIZURE, SELF_EMPLOYED, UNEMPLOYMENT, UNPAID, BIZUM
- **financial_institution**: FINTONIC
- **gateway_payment_status**: PENDING, SUCCEEDED, FAILED
- **gateway_payment_type**: RESERVATION, SERVICE_PAYMENT, VEHICLE_SERVICE_PAYMENT
- **gateway_provider**: STRIPE
- **gearbox_type**: MANUAL, AUTOMATIC
- **gender**: MALE, FEMALE
- **house_types_type**: RENT, ROOM_RENT, PARENTS_ADDRESS, DEED_PAID, DEED_PENDING_PAYMENT, OTHER
- **identification_number_type**: DNI, NIE, CIF
- **installment_status_type**: PENDING, PAID, DELAYED, PAYMENT_PLAN, CANCELLED
- **insurance_types**: NO_INSURANCE, BASIC_LIFE_INSURANCE, LIFE_INSURANCE_PLUS, GAP_INSURANCE, LIFE_INSURANCE_PLUS_GAP
- **interest_ai_next_message_target**: BUYER, SELLER
- **interest_status**: NEW, IN_PROGRESS, PAUSED, DISCARDED, SOLD
- **interest_substatus**: PENDING_EMAIL_SEND, EMAIL_SENT, PENDING_BOT, SENT_TO_BOT, CONTACT_PENDING, MANAGED_BY_CARLOS, CONTACTED, PENDING_TRADE_IN_APPRAISAL, BUDGET_SENT, PENDING_FINANCE_DOCS, PENDING_RESERVATION, TENTATIVE_DELIVERY_DATE, CONFIRMED_DELIVERY_DATE, CERTIFICATION_COMPLETED_AND_SENT, CLIDRIVE_CAR_CHANGE, INTEREST_CHANGE, CLIENT_STOPS_REPLYING, WRONG_CLIENT_DATA, DECISION_POSTPONED, TRADE_IN_PRICE_DISAGREEMENT, MASSIVE_DISCARD, ONLINE_DISTRUST, RESERVATION_REFUND, DATA_DELETION, AD_ERROR, UNREACHABLE, TOO_EXPENSIVE, EXPENSES_TOO_EXPENSIVE, FINANCING_TOO_EXPENSIVE, DUPLICATE_LEAD, WANTS_TO_SEE_CAR, PENDING_OWN_CAR_SALE, NON_FINANCEABLE_PROFILE, NO_STOCK, INTERNAL_TEST, BOUGHT_ELSEWHERE, FINANCING_DENIED, DELIVERED, SERVICE_SOLD, UNSUPPORTED_LOCATION, NO_PHONE, CAR_RESERVED, CAR_SOLD, UNPUBLISHED_VEHICLE, REQUIRES_PHONE_CALL, VEHICLE_LOCATION, VEHICLE_NOT_ELIGIBLE, PROBLEMATIC_CLIENT, PENDING_FINANCING, ACTIVE_FINANCING, PENDING_OWN_BANK_FINANCING, CASH_PAYMENT, IBANCAR_FINANCING, SELLER_REQUEST, PENDING_VISIT
- **invoice_status_type**: PENDING, PAID, UNPAID
- **job_position_type**: EXECUTIVE, QUALIFIED_TECHNICIAN, ADMINISTRATIVE, MANUAL_WORKER, REPRESENTATIVE, SPECIALIST_WORKER, LIBERAL_PROFESSION, PEDDLER, COMMERCIAL, ENGINEER, HEALTHCARE, LEGAL, OTHER
- **legal_nature_type**: NATURAL_PERSON, LEGAL_PERSON
- **length_unit**: KM
- **loan_document_status_type**: SUCCESS, ERROR
- **loan_document_type**: DNI_FRONT, DNI_BACK, NIE_FRONT, NIE_BACK, PASSPORT, INCOME_PROOF, IRPF, BILL
- **loan_purpose_type**: HOME_RENOVATION, NEW_VEHICLE, USED_VEHICLE, HOME_FURNISHING_APPLIANCES, TRAINING, HEALTHCARE, TRAVEL_OR_LEISURE, EVENT_OR_CELEBRATION, NEW_BUSINESS, CASH_FLOW_NEEDS, UNIFY_CREDITS, OTHER
- **offer_status_type**: ONGOING, REJECTED, ARCHIVED, NOT_ALLOWED
- **operation_payment_method**: CASH, FULLY_FINANCED, FINANCED_WITH_DOWN_PAYMENT
- **origin_source_type**: WHATSAPP, WEB, CALL, PARTNER, AFFILIATE, EMAIL, CLIENT_VISIT
- **payment_income_type**: BANK_TRANSFER
- **price_to_market_label_type**: SUPER_PRICE, GOOD_PRICE, FAIR_PRICE
- **price_to_market_types**: SUPER_PRICE, GOOD_PRICE, FAIR_PRICE, HIGH_PRICE, VERY_HIGH_PRICE, PRICE_NOT_PROVIDED
- **professional_activity_type**: AGRICULTURE, EXTRACTIVE_INDUSTRIES, MANUFACTURING, ENERGY_SUPPLY, WATER_SANITATION, CONSTRUCTION, TRADE_REPAIR, TRANSPORT_STORAGE, HOSPITALITY, INFO_COMMUNICATION, FINANCIAL_INSURANCE, REAL_ESTATE, PROFESSIONAL_SCIENTIFIC, PUBLIC_ADMIN_DEFENCE, EDUCATION, HEALTH_SOCIAL_SERVICES, ARTS_ENTERTAINMENT, OTHER_SERVICES, HOUSEHOLD_EMPLOYERS, EXTRATERRITORIAL_ORG
- **professional_status_type**: EMPLOYEE, FREELANCE, UNEMPLOYED, NOT_WORK, PENSIONER, CIVIL_SERVANT, STUDENT
- **purchase_transaction_method_type**: BANK_TRANSFER, ONLINE_PAYMENT, TRADE_IN, DEAL_TRANSFER
- **ref_note_type**: catalogue_vehicle, client, interest
- **repricing_type**: TARGET, AGREED, SENT
- **reservation_cancel_reason_type**: CERTIFICATION_KO, FINAL_CLIENT_DOES_NOT_WANT, CAR_NOT_AVAILABLE, PURCHASED_ELSEWHERE, FINANCING_DENIED, OWNER_DOES_NOT_ANSWER, OWNER_ASKS_FOR_MORE_MONEY, AD_ERROR, TRADE_IN_PRICE_DISAGREEMENT, FINAL_CLIENT_CAR_DEVOLUTION, OWNER_DOES_NOT_WANT_SELL, FINANCING_HUNDRED_PERCENT, OWNER_DELIVERY_DELAY, CLIENT_UNHAPPY_WITH_CERTIFICATION, EXPENSIVE_EXPENSES, CLIENT_DOES_NOT_ANSWER, DECISION_POSTPONED, FINANCING_TOO_EXPENSIVE
- **reservation_method_type**: BANK_TRANSFER, ONLINE_PAYMENT
- **reservation_status_type**: RECEIVED, RETURNED, DISCARDED_NO_REFUND, CHANGE_OF_VEHICLE, CHANGE_OF_CLIENT, RECEIVED_TO_HISTORICAL
- **respondio_attachment_type**: IMAGE, VIDEO, AUDIO, FILE
- **respondio_message_traffic**: INCOMING, OUTGOING
- **respondio_message_type**: TEXT, ATTACHMENT, WHATSAPP_TEMPLATE, QUICK_REPLY
- **respondio_tag_event_action**: ADD, REMOVE
- **respondio_workspace**: C2C_PURCHASES, C2C_SALES
- **service_name**: VEHICLE_CERTIFICATION, MAINLAND_TRANSPORT, BALEARIC_ISLANDS_TRANSPORT, VEHICLE_CLEANING, ADMINISTRATIVE_PROCESSING, CARFAX_REPORT, CARVERTICAL_REPORT, ONE_YEAR_WARRANTY, TWO_YEAR_WARRANTY, THREE_YEAR_WARRANTY, ITP, WARRANTY, PROFESSIONAL_COVERAGE, RELEASE_OF_RETENTION, REPORTS_PACKAGE, SECURE_TRANSACTION_PACKAGE
- **service_scope**: INTEREST, CATALOGUE_VEHICLE
- **service_type**: SINGLE, PACKAGE
- **stage_transition_type**: MANUAL, AUTOMATIC_FORWARD, AUTOMATIC_BACKWARD
- **stage_type**: LEAD_CREATED, LEAD_SENT_TO_BOT, LEAD_PENDING_CALL, LEAD_MANAGED_WITHOUT_CALL, LEAD_CALLED, LEAD_PRE_QUOTED, LEAD_OPPORTUNITY, LEAD_QUOTED, DEAL_CREATED, DEAL_WAITING, DEAL_IN_ANALYSIS, DEAL_PRE_APPROVED, DEAL_APPROVED, DEAL_QUALIFIED, DEAL_WON, DEAL_LOST, CLIENT_CREATED, CLIENT_CANCELLED
- **submission_main_status_type**: PENDING, PROCESSING, PRE_APPROVED, WAITING, IN_ANALYSIS, ACCEPTED, COLLECTED, REJECTED, UNSUCCESSFULLY_APPROVED, EARLY_TERMINATION, RETURN_IN_PROCESS, RETURN, CANCELLED
- **submission_sub_status_type**: PENDING_FORM, PENDING_BANK_VALIDATION, BANK_UNDER_ANALYSIS, PENDING_ADDITIONAL_INFO, PENDING_CO_OWNER, BANK_VALIDATION_ISSUE, PENDING_CUSTOMER_DOC, PENDING_CAR_DOC, PENDING_CONTRACT_SIGNATURE, SIGNED, PENDING_BANK_OFFICE, NON_FINANCEABLE, WITHOUT_CO_OWNER, CLIENT_DESISTS, BANK_VALIDATION_NOT_COMPLETED, CREATED_BY_MISTAKE, PENDING_BANK_VALIDATION_CO_OWNER, CAR_NOT_AVAILABLE, CLIENT_DOES_NOT_ANSWER, SENDING_CAR_DOC_PROFORMA, INCOMPLETE_INFO, DOCUMENT_REVIEW, PENDING_CONFIRMATION, INVOICE_BEING_APPROVED, PENDING_CLIENT_OFFICE, OFFICE_APPOINTMENT_CONFIRMED, ACCEPTED_WITHOUT_APPOINTMENT, ALTERNATIVE_NOT_ACCEPTED, DATA_INCONSISTENCIES, UNREACHABLE, BANK_ANALYSIS_NOT_COMPLETED, CLIENT_WITH_ASNEF, WITH_CO_OWNER, RESUMED_BY_BANK
- **time_unit**: HOURS, MINUTES
- **timing_belt_type**: CHAIN, BELT
- **transferable_vehicle**: YES, NO, INVALID_DOC
- **user_roles**: ADMIN, FINANCIAL_ANALYST, FINANCE_USER, SALES_AGENT, CERTIFIER, COLLECTION_AGENT, APPRAISER, DELIVERIES, PROCESSOR, C2C_SALES_AGENT, MARKETING_AGENT, EXTERNAL_AGENT // Deprecated, SALES_EXTERNAL_AGENT, PROCESSOR_EXTERNAL_AGENT, MANAGER
- **vat_rate_type**: IVA, REBU
- **vehicle_extra_category_type**: MULTIMEDIA, CONFORT, INSIDE, OUTSIDE, SAFETY
- **vehicle_type**: CAR, INDUSTRIAL_VAN