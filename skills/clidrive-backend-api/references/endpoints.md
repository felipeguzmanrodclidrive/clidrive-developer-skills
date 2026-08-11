# Clidrive backend — API endpoints

Generated from `/Users/felipeguzman/Documents/Clidrive/backend` by `gen_endpoints.py`. 339 endpoints across 75 Swagger tags. Regenerate after backend changes rather than editing by hand.

## ai-catalogue-vehicles

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| PATCH | `/ai/v1/catalogue-vehicles/:extId` | updateCatalogueVehicleByExtId | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/catalogue-vehicles/ai-catalogue-vehicles.controller.ts |
| GET | `/ai/v1/catalogue-vehicles/:identifier/taxes` | getCatalogueVehicleTaxes | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/catalogue-vehicles/ai-catalogue-vehicles.controller.ts |

## ai-clients

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/ai/v1/clients/:clientIdentifier/buyer-context` | buyerContext | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/clients/ai-clients-context.controller.ts |
| GET | `/ai/v1/clients/:clientIdentifier/documents` | list | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/clients/ai-clients-documents.controller.ts |
| GET | `/ai/v1/clients/:clientIdentifier/seller-context` | sellerContext | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/clients/ai-clients-context.controller.ts |
| GET | `/ai/v1/clients/:clientIdentifier/submissions` | list | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/clients/ai-clients-submissions.controller.ts |
| GET | `/ai/v1/clients/:clientIdentifier/vehicles-media-originals` | list | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/clients/ai-client-vehicles-media-originals.controller.ts |

## ai-configurations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/ai/v1/configurations/repricing` | repricing | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/configurations/ai-configurations.controller.ts |

## ai-interests

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| PATCH | `/ai/v1/interests/:interestId/interest-ai` | update | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/interests/ai-interests-ai.controller.ts |
| PATCH | `/ai/v1/interests/:interestId/reservations` | update | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/interests/ai-interests-reservations.controller.ts |
| POST | `/ai/v1/interests/:interestId/reservations` | create | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/interests/ai-interests-reservations.controller.ts |
| POST | `/ai/v1/interests/:interestId/reservations/change-client` | changeClient | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/interests/ai-interests-reservations.controller.ts |
| POST | `/ai/v1/interests/:interestId/services/:serviceName` | upsert | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/interests/ai-interests-services.controller.ts |
| PATCH | `/ai/v1/interests/:interestId/submissions` | updateStatus | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/interests/ai-interests-submissions.controller.ts |
| POST | `/ai/v1/interests/:interestId/submissions` | create | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/interests/ai-interests-submissions.controller.ts |
| POST | `/ai/v1/interests/external` | createExternal | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/interests/ai-interests.controller.ts |

## ai-respondio

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/ai/v1/respondio/:clientIdentifier/messages/:workspace` | findMessages | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/respondio/ai-respondio.controller.ts |

## ai-webhooks

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/ai/v1/webhooks/retell/calls` | analyzedCalls |  | apps/svc-clidrive/src/ai/infrastructure/controllers/webhooks/ai-retell-webhook.controller.ts |

## appraisals

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/v1/appraisals` | find | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/appraisals.controller.ts |
| POST | `/v1/appraisals-trade-in` | create | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/appraisals-trade-in.controller.ts |

## asnef

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/v1/asnef` | getAsnefData | ADMIN, DECISION | apps/svc-clidrive/src/client-valuations/infrastructure/controllers/asnef.controller.ts |

## authorization

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/auth/credentials` | createCredential | ADMIN | libs/shared/src/auth/infrastructure/controllers/auth.controller.ts |

## carfax

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/v1/carfax/vehicle-alert` | findVehicleAlert | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/carfax.controller.ts |
| GET | `/v1/carfax/vehicle-data` | findVehicleData | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/carfax.controller.ts |

## catalogue-vehicles

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/catalogue-vehicles` | createCatalogueVehicle | ADMIN, DECISION | apps/svc-clidrive/src/catalogue-vehicles/infrastructure/controllers/catalogue-vehicles.controller.ts |
| PUT | `/v1/catalogue-vehicles/:extId/carfax` | updateCatalogueVehicleFromCarfaxByExtId | ADMIN, DECISION | apps/svc-clidrive/src/catalogue-vehicles/infrastructure/controllers/catalogue-vehicles.controller.ts |
| PUT | `/v1/catalogue-vehicles/:extId/clients` | updateCatalogueVehicleClientByExtId | ADMIN, DECISION | apps/svc-clidrive/src/catalogue-vehicles/infrastructure/controllers/catalogue-vehicles.controller.ts |
| GET | `/v1/catalogue-vehicles/:extId/sheet` | getCatalogueVehicleSheetByExtId | ADMIN, DECISION | apps/svc-clidrive/src/catalogue-vehicles/infrastructure/controllers/catalogue-vehicles.controller.ts |

## certifications

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/certifications` | createCertification | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/certifications/ai-certifications.controller.ts |
| GET | `/v1/certifications/:extId` | getCertification | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/certifications/ai-certifications.controller.ts |
| PATCH | `/v1/certifications/:extId` | cancelCertification | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/certifications/ai-certifications.controller.ts |
| PATCH | `/v1/certifications/:extId/sellers` | updateSeller | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/certifications/ai-certifications.controller.ts |
| GET | `/v1/certifications/availability` | getAvailability | ADMIN, AI | apps/svc-clidrive/src/ai/infrastructure/controllers/certifications/ai-certifications.controller.ts |

## client-blacklist

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/client-blacklist` | addToBlacklist | ADMIN | apps/svc-clidrive/src/client-blacklist/infrastructure/controllers/client-blacklist.controller.ts |

## client-calls

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/client-calls` | initiateCall | ADMIN, DECISION | apps/svc-clidrive/src/client-calls/infrastructure/controllers/client-calls.controller.ts |

## client-calls-webhooks

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/client-calls/webhooks/twilio/call-recordings` | callRecording |  | apps/svc-clidrive/src/client-calls/infrastructure/controllers/client-calls-webhook.controller.ts |
| POST | `/v1/client-calls/webhooks/twilio/voice` | incomingCall |  | apps/svc-clidrive/src/client-calls/infrastructure/controllers/client-calls-webhook.controller.ts |

## connect

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/statistics` | calculateStatistics | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect.controller.ts |

## connect-catalogue-vehicle-documents

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/connect/v1/catalogue-vehicles` | createCatalogueVehicleDocument | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-documents.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/:uuid/documents` | listCatalogueVehicleDocuments | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-documents.controller.ts |
| POST | `/connect/v1/catalogue-vehicles/:uuid/documents` | confirmCatalogueVehicleDocumentUpload | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-documents.controller.ts |
| DELETE | `/connect/v1/catalogue-vehicles/:uuid/documents/:documentUuid` | deleteCatalogueVehicleDocument | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-documents.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/:uuid/documents/:documentUuid/preview-url` | getCatalogueVehicleDocumentPreviewUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-documents.controller.ts |
| PATCH | `/connect/v1/catalogue-vehicles/:uuid/documents/:documentUuid/restore` | restoreCatalogueVehicleDocument | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-documents.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/:uuid/documents/upload-url` | getCatalogueVehicleDocumentUploadUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-documents.controller.ts |

## connect-catalogue-vehicle-images

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| DELETE | `/connect/v1/catalogue-vehicle-images/:uuid` | deleteCatalogueVehicleImage | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-images.controller.ts |
| PUT | `/connect/v1/catalogue-vehicle-images/:uuid` | updateCatalogueVehicleImage | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-images.controller.ts |
| POST | `/connect/v1/catalogue-vehicle-images/upload` | uploadCatalogueVehicleImages | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-images.controller.ts |

## connect-catalogue-vehicle-notification-history

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/catalogue-vehicle-notification-history` | getCatalogueVehicleNotificationHistory | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-notification-history.controller.ts |

## connect-catalogue-vehicles

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehicle | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehicleDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehiclePerformance | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehicleExtras | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehicleInspection | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getNextCatalogueVehicleStatuses | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehicleStatusTransitions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getClientByCatalogueVehicleUuid | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | GetCatalogueVehicleRepricing | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getPublicationDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehicleMissingFieldsToPublish | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehicleMissingFieldsToBuy | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehicleImages | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCatalogueVehicleMultipublisherErrors | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | getCarfaxVehicleData | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles` | findCatalogueVehicleClientHistoryByVehicleUuid | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| POST | `/connect/v1/catalogue-vehicles` | createCatalogueVehicle | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| POST | `/connect/v1/catalogue-vehicles` | createNextCatalogueVehicleStatuses | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| POST | `/connect/v1/catalogue-vehicles` | createCatalogueVehicleManagedAd | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| POST | `/connect/v1/catalogue-vehicles` | createCatalogueVehicleRepricing | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| POST | `/connect/v1/catalogue-vehicles` | createTradeInCatalogueVehicle | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| PUT | `/connect/v1/catalogue-vehicles` | updateCatalogueVehicleDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| PUT | `/connect/v1/catalogue-vehicles` | updateCatalogueVehiclePerformance | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| PUT | `/connect/v1/catalogue-vehicles` | updateCatalogueVehicleExtras | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| PUT | `/connect/v1/catalogue-vehicles` | updateCatalogueVehicleInspection | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| PUT | `/connect/v1/catalogue-vehicles` | updateCatalogueVehicleManagedAd | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| PUT | `/connect/v1/catalogue-vehicles` | changeDealClient | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| PUT | `/connect/v1/catalogue-vehicles` | updateCatalogueVehicleAgents | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| PUT | `/connect/v1/catalogue-vehicles` | updateCatalogueVehicleProcessor | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| POST | `/connect/v1/catalogue-vehicles/:catalogueVehicleUuid/note` | createCatalogueVehicleNote | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-notes.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/:catalogueVehicleUuid/notes` | getCatalogueVehiclesNotes | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-notes.controller.ts |
| PATCH | `/connect/v1/catalogue-vehicles/:catalogueVehicleUuid/notes/:noteUuid` | updateCatalogueVehicleNote | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicle-notes.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/:uuid/buy-contract` | getCatalogueVehicleBuyContract | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/:uuid/c2c-buy-sell-contract` | getCatalogueVehicleC2cBuySellContract | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/:uuid/services` | findAll | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/connect-catalogue-vehicle-services.controller.ts |
| POST | `/connect/v1/catalogue-vehicles/:uuid/services` | create | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/connect-catalogue-vehicle-services.controller.ts |
| DELETE | `/connect/v1/catalogue-vehicles/:uuid/services/:id` | delete | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/connect-catalogue-vehicle-services.controller.ts |
| PATCH | `/connect/v1/catalogue-vehicles/:uuid/services/:id` | update | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/connect-catalogue-vehicle-services.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/:uuid/sheet` | getCatalogueVehicleSheetByExtId | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| POST | `/connect/v1/catalogue-vehicles/bulk-appraisal` | bulkAppraisal | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| POST | `/connect/v1/catalogue-vehicles/bulk-create` | bulkCreation | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| POST | `/connect/v1/catalogue-vehicles/bulk-price-update` | bulkUpdate | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/statistics` | calculateVehiclesStatistics | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |
| GET | `/connect/v1/catalogue-vehicles/sub-statuses` | getSubStatusesMap | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/catalogue-vehicles.controller.ts |

## connect-certifications

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/certifications` | findAll | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications.controller.ts |
| POST | `/connect/v1/certifications` | createCertification | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications.controller.ts |
| GET | `/connect/v1/certifications/:uuid` | findOne | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications.controller.ts |
| PATCH | `/connect/v1/certifications/:uuid` | update | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications.controller.ts |
| POST | `/connect/v1/certifications/:uuid/documents` | confirmDocumentUpload | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications.controller.ts |
| GET | `/connect/v1/certifications/:uuid/documents/:documentUuid/preview-url` | getDocumentPreviewUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications.controller.ts |
| GET | `/connect/v1/certifications/:uuid/documents/upload-url` | getDocumentUploadUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications.controller.ts |
| GET | `/connect/v1/certifications/certifiers` | getCertifiers | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications-certifiers.controller.ts |
| GET | `/connect/v1/certifications/certifiers/:certifierUserUuid/availability/:date` | getSlots | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications-certifiers.controller.ts |
| DELETE | `/connect/v1/certifications/slots` | deleteSlots | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications-slots.controller.ts |
| GET | `/connect/v1/certifications/slots` | findAll | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications-slots.controller.ts |
| POST | `/connect/v1/certifications/slots/ranges` | createRanges | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications-slots.controller.ts |
| PUT | `/connect/v1/certifications/slots/ranges` | replaceRanges | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications-slots.controller.ts |
| GET | `/connect/v1/certifications/templates` | findAll | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications-templates.controller.ts |
| POST | `/connect/v1/certifications/templates` | create | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications-templates.controller.ts |
| PATCH | `/connect/v1/certifications/templates/:certificationTemplateUuid` | update | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/certifications/connect-certifications-templates.controller.ts |

## connect-changelog

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/changelog` | getChangelog | ADMIN | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-changelog.controller.ts |

## connect-clients

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/clients` | findClients | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients.controller.ts |
| POST | `/connect/v1/clients` | createClient | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients.controller.ts |
| GET | `/connect/v1/clients/:uuid` | findOne | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients.controller.ts |
| PATCH | `/connect/v1/clients/:uuid` | patchClient | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients.controller.ts |
| GET | `/connect/v1/clients/:uuid/ai-voice-calls` | findAiVoiceCalls | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-ai-voice-calls.controller.ts |
| GET | `/connect/v1/clients/:uuid/calls` | findClientCalls | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-calls.controller.ts |
| GET | `/connect/v1/clients/:uuid/co-owner` | findCoOwner | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-co-owners.controller.ts |
| PUT | `/connect/v1/clients/:uuid/co-owner` | upsertCoOwner | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-co-owners.controller.ts |
| GET | `/connect/v1/clients/:uuid/documents` | listClientDocuments | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-documents.controller.ts |
| POST | `/connect/v1/clients/:uuid/documents` | confirmClientDocumentUpload | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-documents.controller.ts |
| DELETE | `/connect/v1/clients/:uuid/documents/:documentUuid` | deleteClientDocument | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-documents.controller.ts |
| GET | `/connect/v1/clients/:uuid/documents/:documentUuid/preview-url` | getClientDocumentPreviewUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-documents.controller.ts |
| PATCH | `/connect/v1/clients/:uuid/documents/:documentUuid/restore` | restoreClientDocument | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-documents.controller.ts |
| GET | `/connect/v1/clients/:uuid/documents/upload-url` | getClientDocumentUploadUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-client-documents.controller.ts |
| PUT | `/connect/v1/clients/:uuid/external-ids/:key` | putClientExternalId | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients.controller.ts |

## connect-clients-notes

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/connect/v1/clients/:clientUuid/notes` | createNote | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-notes.controller.ts |
| DELETE | `/connect/v1/clients/:clientUuid/notes/:noteUuid` | deleteNote | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-notes.controller.ts |
| GET | `/connect/v1/clients/:clientUuid/notes/:noteUuid` | getNoteDetail | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-notes.controller.ts |
| PATCH | `/connect/v1/clients/:clientUuid/notes/:noteUuid` | updateNote | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-notes.controller.ts |
| GET | `/connect/v1/clients/:clientUuid/notes/:noteUuid/attachment-upload-url` | getNoteAttachmentUploadUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-notes.controller.ts |
| POST | `/connect/v1/clients/:clientUuid/notes/:noteUuid/attachments` | addNoteAttachment | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-notes.controller.ts |
| DELETE | `/connect/v1/clients/:clientUuid/notes/:noteUuid/attachments/:attachmentUuid` | deleteNoteAttachment | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-notes.controller.ts |
| GET | `/connect/v1/clients/:clientUuid/notes/:noteUuid/attachments/:attachmentUuid/download-url` | getNoteAttachmentDownloadUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-notes.controller.ts |
| GET | `/connect/v1/clients/:uuid/notes` | getNotesInClient | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-notes.controller.ts |

## connect-clients-submissions

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/clients/:clientUuid/submissions` | getSubmissions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/clients/connect-clients-submissions.controller.ts |

## connect-configurations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/configurations/:id` | getConfiguration | ADMIN, CONNECT | apps/svc-clidrive/src/configurations/infrastructure/controllers/connect-configuration.controller.ts |
| PUT | `/connect/v1/configurations/:id` | updateConfiguration | ADMIN, CONNECT | apps/svc-clidrive/src/configurations/infrastructure/controllers/connect-configuration.controller.ts |

## connect-deal-calculator

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| PATCH | `/connect/v1/deals/:dealUuid/offers/:uuid` | patchOffer | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-calculator.controller.ts |
| GET | `/connect/v1/deals/:uuid/offers` | getOffers | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-calculator.controller.ts |
| POST | `/connect/v1/deals/:uuid/offers` | calculateOffers | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-calculator.controller.ts |
| GET | `/connect/v1/deals/:uuid/preoffer` | getPreoffer | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-calculator.controller.ts |

## connect-deal-car-delivery

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals/:dealUuid/delivery` | getCarDelivery | ADMIN, CONNECT | apps/svc-clidrive/src/car-deliveries/infrastructure/controllers/connect-deal-car-delivery.controller.ts |
| PUT | `/connect/v1/deals/:dealUuid/delivery` | upsertCarDelivery | ADMIN, CONNECT | apps/svc-clidrive/src/car-deliveries/infrastructure/controllers/connect-deal-car-delivery.controller.ts |

## connect-deal-catalogue-vehicle

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals/:dealUuid/catalogue-vehicle` | getReservation | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/catalogue-vehicles/deal-catalogue-vehicle.controller.ts |

## connect-deal-notes

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals/:dealUuid/notes` | getDealNotes | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| POST | `/connect/v1/deals/:dealUuid/notes` | createDealNote | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| DELETE | `/connect/v1/deals/:dealUuid/notes/:noteUuid` | deleteDealNote | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| GET | `/connect/v1/deals/:dealUuid/notes/:noteUuid` | getDealNote | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| PATCH | `/connect/v1/deals/:dealUuid/notes/:noteUuid` | updateDealNote | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| GET | `/connect/v1/deals/:dealUuid/notes/:noteUuid/attachment-upload-url` | getNoteAttachmentUploadUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| POST | `/connect/v1/deals/:dealUuid/notes/:noteUuid/attachments` | addNoteAttachment | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| DELETE | `/connect/v1/deals/:dealUuid/notes/:noteUuid/attachments/:attachmentUuid` | deleteDealNoteAttachment | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| GET | `/connect/v1/deals/:dealUuid/notes/:noteUuid/attachments/:attachmentUuid/download-url` | getNoteAttachmentDownloadUrl | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| PUT | `/connect/v1/deals/:dealUuid/notes/:noteUuid/is-pinned` | updateDealNoteIsPinned | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |
| GET | `/connect/v1/deals/:dealUuid/pinned-notes` | getDealPinnedNotes | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-notes.controller.ts |

## connect-deal-purchase-discounts

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals/:dealUuid/purchase-discounts` | getPurchaseDiscounts | ADMIN, CONNECT | apps/svc-clidrive/src/purchase-discounts/infrastructure/controllers/connect-purchase-discounts.controller.ts |
| POST | `/connect/v1/deals/:dealUuid/purchase-discounts` | createPurchaseDiscount | ADMIN, CONNECT | apps/svc-clidrive/src/purchase-discounts/infrastructure/controllers/connect-purchase-discounts.controller.ts |
| DELETE | `/connect/v1/deals/:dealUuid/purchase-discounts/:uuid` | deletePurchaseDiscount | ADMIN, CONNECT | apps/svc-clidrive/src/purchase-discounts/infrastructure/controllers/connect-purchase-discounts.controller.ts |
| PUT | `/connect/v1/deals/:dealUuid/purchase-discounts/:uuid` | updatePurchaseDiscount | ADMIN, CONNECT | apps/svc-clidrive/src/purchase-discounts/infrastructure/controllers/connect-purchase-discounts.controller.ts |

## connect-deal-purchase-transactions

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals/:dealUuid/purchase-transactions` | getPurchaseTransactions | ADMIN, CONNECT | apps/svc-clidrive/src/purchase-transactions/infrastructure/controllers/connect-deal-purchase-transactions.controller.ts |
| POST | `/connect/v1/deals/:dealUuid/purchase-transactions` | createPurchaseTransaction | ADMIN, CONNECT | apps/svc-clidrive/src/purchase-transactions/infrastructure/controllers/connect-deal-purchase-transactions.controller.ts |
| DELETE | `/connect/v1/deals/:dealUuid/purchase-transactions/:purchaseTransactionUuid` | deletePurchaseTransaction | ADMIN, CONNECT | apps/svc-clidrive/src/purchase-transactions/infrastructure/controllers/connect-deal-purchase-transactions.controller.ts |
| PUT | `/connect/v1/deals/:dealUuid/purchase-transactions/:uuid` | updatePurchaseTransaction | ADMIN, CONNECT | apps/svc-clidrive/src/purchase-transactions/infrastructure/controllers/connect-deal-purchase-transactions.controller.ts |

## connect-deal-reservations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals/:dealUuid/reservation` | getReservation | ADMIN, CONNECT | apps/svc-clidrive/src/reservations/infrastructure/controllers/connect-deal-reservations.controller.ts |
| POST | `/connect/v1/deals/:dealUuid/reservation` | createReservation | ADMIN, CONNECT | apps/svc-clidrive/src/reservations/infrastructure/controllers/connect-deal-reservations.controller.ts |
| PUT | `/connect/v1/deals/:dealUuid/reservation/:uuid` | updateReservation | ADMIN, CONNECT | apps/svc-clidrive/src/reservations/infrastructure/controllers/connect-deal-reservations.controller.ts |

## connect-deal-submissions

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals/:dealUuid/submissions` | getSubmissions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-submissions.controller.ts |
| GET | `/connect/v1/deals/:dealUuid/submissions/:uuid` | getSubmission | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-submissions.controller.ts |
| PATCH | `/connect/v1/deals/:dealUuid/submissions/:uuid` | updateSubmission | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-submissions.controller.ts |
| GET | `/connect/v1/deals/:dealUuid/submissions/:uuid/status-transitions` | getSubmissionStatusTransitions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-submissions.controller.ts |
| POST | `/connect/v1/deals/:dealUuid/submissions/:uuid/status-transitions` | createSubmissionStatusTransition | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-submissions.controller.ts |
| GET | `/connect/v1/deals/:dealUuid/submissions/:uuid/statuses` | getNextSubmissionMainStatuses | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-submissions.controller.ts |

## connect-deal-valuations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals/:uuid/alerts` | getAlerts | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-valuations.controller.ts |
| GET | `/connect/v1/deals/:uuid/appraisals` | getAppraisals | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-valuations.controller.ts |

## connect-deals

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals` | find | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals` | getClientByDealUuid | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| POST | `/connect/v1/deals` | create | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid` | getDealByUuid | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PATCH | `/connect/v1/deals/:uuid` | updateDeal | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/addresses` | getAddresses | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/addresses` | updateAddresses | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/bank-details` | getBankDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/bank-details` | updateBankDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/basic-info` | getDealBasicInfo | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/c2c-metrics` | getDealC2CMetrics | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/client` | changeDealClient | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/documentation-link` | getDocumentationLink | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/documentation-link` | updateDocumentationLink | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/employment` | getEmployment | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/employment` | updateEmployment | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/foreign-details` | getForeignDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/foreign-details` | updateForeignDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/mkt-details` | getMktDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/personal-details` | getPersonalDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/personal-details` | updatePersonalDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/proforma` | getDealProforma | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/sell-contract` | getCatalogueVehicleSellContract | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/situation` | updateDealSituation | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/stage` | updateDealStage | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/vehicle` | getVehicle | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/vehicle` | updateVehicle | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| PUT | `/connect/v1/deals/:uuid/vehicle/license-plate` | changeVehicle | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |
| GET | `/connect/v1/deals/:uuid/warranty-order` | getDealWarrantyOrder | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deals.controller.ts |

## connect-financial-aggregations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| PATCH | `/connect/v1/deals/:dealUuid/financial-aggregations/:financialAggregationUuid` | updateFinancialAggregation | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-financial-aggregations.controller.ts |
| GET | `/connect/v1/deals/:uuid/financial-aggregations` | findFinancialAggregationsByDeal | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-financial-aggregations.controller.ts |
| POST | `/connect/v1/deals/:uuid/financial-aggregations` | createFinancialAggregation | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-deal-financial-aggregations.controller.ts |

## connect-interest-purchase-discounts

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/interests/:interestUuid/purchase-discounts` | getPurchaseDiscounts | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-purchase-discounts.controller.ts |
| POST | `/connect/v1/interests/:interestUuid/purchase-discounts` | createPurchaseDiscount | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-purchase-discounts.controller.ts |
| DELETE | `/connect/v1/interests/:interestUuid/purchase-discounts/:uuid` | deletePurchaseDiscount | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-purchase-discounts.controller.ts |
| PUT | `/connect/v1/interests/:interestUuid/purchase-discounts/:uuid` | updatePurchaseDiscount | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-purchase-discounts.controller.ts |

## connect-interests

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/interests` | find | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |
| POST | `/connect/v1/interests` | create | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |
| GET | `/connect/v1/interests/:uuid` | findOne | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |
| PATCH | `/connect/v1/interests/:uuid` | updateInterest | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |
| GET | `/connect/v1/interests/:uuid/catalogue-vehicle` | getCatalogueVehicle | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-catalogue-vehicle.controller.ts |
| POST | `/connect/v1/interests/:uuid/financial-services` | create | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interest-financial-services.controller.ts |
| PUT | `/connect/v1/interests/:uuid/financial-services/:financialServiceUuid` | update | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interest-financial-services.controller.ts |
| GET | `/connect/v1/interests/:uuid/metrics` | getInterestMetrics |  | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-metrics.controller.ts |
| GET | `/connect/v1/interests/:uuid/mkt` | getMktDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-mkt.controller.ts |
| GET | `/connect/v1/interests/:uuid/proforma` | getProforma | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-proforma.controller.ts |
| GET | `/connect/v1/interests/:uuid/purchase-transactions` | getPurchaseTransactions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-purchase-transactions.controller.ts |
| POST | `/connect/v1/interests/:uuid/purchase-transactions` | createPurchaseTransaction | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-purchase-transactions.controller.ts |
| DELETE | `/connect/v1/interests/:uuid/purchase-transactions/:purchaseTransactionUuid` | deletePurchaseTransaction | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-purchase-transactions.controller.ts |
| PUT | `/connect/v1/interests/:uuid/purchase-transactions/:purchaseTransactionUuid` | updatePurchaseTransaction | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-purchase-transactions.controller.ts |
| GET | `/connect/v1/interests/:uuid/sell-contract` | getSellContract | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-sell-contract.controller.ts |
| GET | `/connect/v1/interests/:uuid/services` | findAll | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interest-services.controller.ts |
| POST | `/connect/v1/interests/:uuid/services` | create | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interest-services.controller.ts |
| PATCH | `/connect/v1/interests/:uuid/services/:id` | update | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interest-services.controller.ts |
| PUT | `/connect/v1/interests/:uuid/status` | updateInterestStatus | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |
| GET | `/connect/v1/interests/:uuid/taxes` | getInterestItpTaxes | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |
| POST | `/connect/v1/interests/:uuid/taxes` | calculateInterestItpTaxes | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |
| GET | `/connect/v1/interests/:uuid/warranty-order` | getWarrantyOrder | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-warranty-order.controller.ts |
| GET | `/connect/v1/interests/main-interest/:clientUuid` | getMainInterest | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |
| PUT | `/connect/v1/interests/main-interest/:interestId` | setMainInterest | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |
| GET | `/connect/v1/interests/statistics` | calculateInterestsStatistics | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests.controller.ts |

## connect-interests-calculator

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| PATCH | `/connect/v1/interests/:interestUuid/offers/:uuid` | patchOffer | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interest-calculator.controller.ts |
| GET | `/connect/v1/interests/:uuid/offers` | getOffers | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interest-calculator.controller.ts |
| POST | `/connect/v1/interests/:uuid/offers` | calculateOffers | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interest-calculator.controller.ts |

## connect-interests-delivery

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/interests/:interestUuid/delivery` | getCarDelivery | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-delivery.controller.ts |
| POST | `/connect/v1/interests/:interestUuid/delivery` | upsertCarDelivery | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-delivery.controller.ts |

## connect-interests-submissions

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/interests/:interestUuid/submissions` | getSubmissions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-submissions.controller.ts |
| GET | `/connect/v1/interests/:interestUuid/submissions/:uuid` | getSubmission | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-submissions.controller.ts |
| PATCH | `/connect/v1/interests/:interestUuid/submissions/:uuid` | updateSubmission | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-submissions.controller.ts |
| POST | `/connect/v1/interests/:interestUuid/submissions/:uuid/documents` | uploadDocument | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-submissions.controller.ts |
| POST | `/connect/v1/interests/:interestUuid/submissions/:uuid/loans` | startLoanFromSubmission | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-submissions.controller.ts |
| GET | `/connect/v1/interests/:interestUuid/submissions/:uuid/loans/missing-fields` | getSubmissionMissingFieldsToCreateLoan | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-submissions.controller.ts |
| GET | `/connect/v1/interests/:interestUuid/submissions/:uuid/status-transitions` | getSubmissionStatusTransitions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-submissions.controller.ts |
| POST | `/connect/v1/interests/:interestUuid/submissions/:uuid/status-transitions` | createSubmissionStatusTransition | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-submissions.controller.ts |
| GET | `/connect/v1/interests/:interestUuid/submissions/:uuid/statuses` | getNextSubmissionMainStatuses | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-submissions.controller.ts |

## connect-locations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/locations/provinces` | getProvinces | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-locations.controller.ts |

## connect-payment-breakdowns

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| PUT | `/connect/v1/payment-breakdowns/:uuid` | updatePaymentBreakdown | ADMIN, CONNECT | apps/svc-clidrive/src/payment-breakdowns/infrastructure/controllers/connect-payment-breakdowns.controller.ts |
| GET | `/connect/v1/payment-breakdowns/catalogue-vehicle/:catalogueVehicleUuid` | getPaymentBreakdownsByCatalogueVehicle | ADMIN, CONNECT | apps/svc-clidrive/src/payment-breakdowns/infrastructure/controllers/connect-payment-breakdowns.controller.ts |
| POST | `/connect/v1/payment-breakdowns/catalogue-vehicle/:catalogueVehicleUuid` | createPaymentBreakdown | ADMIN, CONNECT | apps/svc-clidrive/src/payment-breakdowns/infrastructure/controllers/connect-payment-breakdowns.controller.ts |

## connect-rent-deal

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/deals/:uuid/rent-tracking-details` | getTrackingDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-rent-deal.controller.ts |
| PUT | `/connect/v1/deals/:uuid/rent-tracking-details` | updateTrackingDetails | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-rent-deal.controller.ts |
| GET | `/connect/v1/deals/:uuid/vehicle-inspection` | getVehicleInspection | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-rent-deal.controller.ts |
| PUT | `/connect/v1/deals/:uuid/vehicle-inspection` | updateVehicleInspection | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-rent-deal.controller.ts |

## connect-reservations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/reservations` | getReservation | ADMIN, CONNECT | apps/svc-clidrive/src/reservations/infrastructure/controllers/connect-reservations.controller.ts |

## connect-respondio

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/respondio/attachments` | downloadAttachments | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/respondio/connect-respondio.controller.ts |
| GET | `/connect/v1/respondio/messages` | findMessages | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/respondio/connect-respondio.controller.ts |

## connect-services

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/services` | findAll | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/services/connect-services.controller.ts |
| PATCH | `/connect/v1/services/:uuid` | update | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/services/connect-services.controller.ts |

## connect-submissions

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/submissions` | getSubmissions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-submissions.controller.ts |

## connect-users

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/users` | findUsers | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-users.controller.ts |
| PATCH | `/connect/v1/users/:uuid` | updateUser | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-users.controller.ts |
| GET | `/connect/v1/users/me` | findUser | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-users.controller.ts |

## connect-vehicle-features

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/connect/v1/vehicle-features/colors` | getColors | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-vehicle-features.controller.ts |
| GET | `/connect/v1/vehicle-features/jato-versions` | getJatoVersions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-vehicle-features.controller.ts |
| GET | `/connect/v1/vehicle-features/makes` | getMakes | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-vehicle-features.controller.ts |
| GET | `/connect/v1/vehicle-features/models` | getModels | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-vehicle-features.controller.ts |
| POST | `/connect/v1/vehicle-features/models` | createModel | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-vehicle-features.controller.ts |
| GET | `/connect/v1/vehicle-features/versions` | getVersions | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-vehicle-features.controller.ts |
| POST | `/connect/v1/vehicle-features/versions` | createVersion | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/connect-vehicle-features.controller.ts |

## deals

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/v2/deals` | find | ADMIN, DECISION | apps/svc-clidrive/src/deals/infrastructure/controllers/deals.v2.controller.ts |
| GET | `/v2/deals/:id` | findOne | ADMIN, DECISION | apps/svc-clidrive/src/deals/infrastructure/controllers/deals.v2.controller.ts |

## external-vehicles

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/external-vehicles/providers/:provider/sync` | syncExternalVehicle | ADMIN | apps/svc-clidrive/src/external-vehicles/infrastructure/controllers/external-vehicles.controller.ts |

## financial-aggregations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| PATCH | `/v1/financial-aggregations/:financialAggregationUuid/product/:productUuid/transactions` | updateProductTransactions | ADMIN, DECISION | apps/svc-clidrive/src/financial-aggregations/infrastructure/controllers/financial-aggregation.controller.ts |
| GET | `/v1/financial-aggregations/:uuid` | getFinancialAggregationByUUID | ADMIN, DECISION | apps/svc-clidrive/src/financial-aggregations/infrastructure/controllers/financial-aggregation.controller.ts |

## ganvam

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/v1/ganvam` | find | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/ganvam.controller.ts |
| GET | `/v1/ganvam/fuels` | fuels | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/ganvam.controller.ts |
| GET | `/v1/ganvam/models` | models | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/ganvam.controller.ts |
| GET | `/v1/ganvam/years` | years | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/ganvam.controller.ts |

## interests

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/v1/interests` | find | ADMIN, DECISION | apps/svc-clidrive/src/interests/infrastructure/controllers/interests.controller.ts |
| GET | `/v1/interests/:id` | findOne | ADMIN, DECISION | apps/svc-clidrive/src/interests/infrastructure/controllers/interests.controller.ts |

## interests-reservations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/connect/v1/interests/:interestUuid/reservations` | createReservationForInterest | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-reservations.controller.ts |
| PATCH | `/connect/v1/interests/:uuid/reservations` | updateInterestReservation | ADMIN, CONNECT | apps/svc-clidrive/src/connect/infrastructure/controllers/interests/connect-interests-reservations.controller.ts |

## marketplace

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/marketplace/v1/financing/installments` | getInstallments | WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-financing.controller.ts |
| POST | `/marketplace/v1/financing/requests` | createFinancingRequest | WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-financing.controller.ts |

## marketplace-appraisals

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/marketplace/v1/appraisals` | create | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-appraisals.controller.ts |

## marketplace-catalogue-vehicles

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/marketplace/v1/catalogue-vehicles` | getCatalogueVehicles | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-catalogue-vehicles.controller.ts |
| GET | `/marketplace/v1/catalogue-vehicles/:extId` | getCatalogueVehicleByExtId | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-catalogue-vehicles.controller.ts |
| GET | `/marketplace/v1/catalogue-vehicles/:extId/installments` | getInstallments | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-catalogue-vehicles.controller.ts |
| GET | `/marketplace/v1/catalogue-vehicles/:extId/payment-context` | getCatalogueVehiclePaymentContextByExtId | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-catalogue-vehicles.controller.ts |
| POST | `/marketplace/v1/catalogue-vehicles/:extId/services/:name/payment-intent` | createPaymentIntentForServicePayment | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-catalogue-vehicles.controller.ts |
| POST | `/marketplace/v1/catalogue-vehicles/:extId/views` | recordView | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-catalogue-vehicles.controller.ts |
| GET | `/marketplace/v1/catalogue-vehicles/filter-options` | getFilterOptions | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-catalogue-vehicles.controller.ts |
| GET | `/marketplace/v1/catalogue-vehicles/for-sitemap` | getAllCatalogueVehiclesForSitemap | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-catalogue-vehicles.controller.ts |

## marketplace-features

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/marketplace/v1/features/makes` | getMakes | WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-features.controller.ts |
| GET | `/marketplace/v1/features/models` | getModels | WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-features.controller.ts |

## marketplace-interests

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/marketplace/v1/interests` | create | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-interests.controller.ts |
| GET | `/marketplace/v1/interests/:uuid/payment-context` | getPaymentContext | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-interests.controller.ts |
| POST | `/marketplace/v1/interests/certification` | createCertification | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-interests.controller.ts |
| POST | `/marketplace/v1/interests/free-reservation` | createFreeReservation | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-interests.controller.ts |

## marketplace-marketing

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/marketplace/v1/marketing/event` | trackEvent | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-marketing.controller.ts |

## marketplace-reservations

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/marketplace/v1/reservations/payment-intent` | createPaymentIntent | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-reservations.controller.ts |

## marketplace-services

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/marketplace/v1/services` | findAllServices | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-services.controller.ts |
| POST | `/marketplace/v1/services/:name/payment-intent` | createPaymentIntent | ADMIN, WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-services.controller.ts |

## marketplace-stripe-webhooks

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/marketplace/v1/stripe/webhooks/payment-intent` | handlePaymentIntent |  | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-stripe-webhooks.controller.ts |
| POST | `/marketplace/v1/stripe/webhooks/payment-intent/vehicle-services` | handlePaymentIntentVehicleServicePayment |  | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-stripe-webhooks.controller.ts |

## motor-es

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/v1/motor-es` | find | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/motor-es.controller.ts |
| GET | `/v1/motor-es/similarity` | similarity | ADMIN, DECISION | apps/svc-clidrive/src/vehicle-valuations/infrastructure/controllers/motor-es.controller.ts |

## multipublisher

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/multipublisher/cochesnet/manual-match/:uuid` | manualCochesnetAdMatch | ADMIN | apps/svc-clidrive/src/multipublisher/infrastructure/controllers/multipublisher.controller.ts |
| POST | `/v1/multipublisher/cochesnet/republish/:uuid` | republishCochesnetAds | ADMIN | apps/svc-clidrive/src/multipublisher/infrastructure/controllers/multipublisher.controller.ts |
| POST | `/v1/multipublisher/resync-ads/:uuid` | resyncAds | ADMIN | apps/svc-clidrive/src/multipublisher/infrastructure/controllers/multipublisher.controller.ts |
| POST | `/v1/multipublisher/sumauto/republish/:uuid` | republishSumautoAds | ADMIN | apps/svc-clidrive/src/multipublisher/infrastructure/controllers/multipublisher.controller.ts |
| PATCH | `/v1/multipublisher/sumauto/vehicle-models/sumauto-id` | assignSumautoIdToVehicleModel | ADMIN | apps/svc-clidrive/src/multipublisher/infrastructure/controllers/multipublisher.controller.ts |

## multipublisher-publisher

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/v1/multipublisher/wallapop/authorize` | wallapopAuthorize | ADMIN | apps/svc-clidrive/src/multipublisher/infrastructure/controllers/multipublisher-publishers.controller.ts |
| GET | `/v1/multipublisher/wallapop/redirect-uri` | wallapopRedirectUri | ADMIN | apps/svc-clidrive/src/multipublisher/infrastructure/controllers/multipublisher-publishers.controller.ts |

## nps-forms

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/nps/v1/forms/:publicId` | getForm | WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-nps-forms.controller.ts |
| PATCH | `/nps/v1/forms/:publicId` | submitForm | WEB | apps/svc-clidrive/src/marketplace/infrastructure/controllers/marketplace-nps-forms.controller.ts |

## respondio

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/respondio/webhook/incoming-msg` | handleIncomingMsgWebhook |  | apps/svc-clidrive/src/respondio/infrastructure/controllers/respondio.controller.ts |
| POST | `/v1/respondio/webhook/outgoing-msg` | handleOutgoingMsgWebhook |  | apps/svc-clidrive/src/respondio/infrastructure/controllers/respondio.controller.ts |

## submission-loans

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/submission-loans/:financier` | createLoan | ADMIN, DECISION | apps/svc-clidrive/src/submissions/infrastructure/controllers/submission-loans.controller.ts |
| GET | `/v1/submission-loans/:financier/:uuid` | getLoanByUuid | ADMIN, DECISION | apps/svc-clidrive/src/submissions/infrastructure/controllers/submission-loans.controller.ts |
| POST | `/v1/submission-loans/:financier/:uuid/documents` | uploadDocument | ADMIN, DECISION | apps/svc-clidrive/src/submissions/infrastructure/controllers/submission-loans.controller.ts |
| GET | `/v1/submission-loans/:financier/interests/:interestId/missing-fields` | getMissingFieldsToCreateLoan | ADMIN, DECISION | apps/svc-clidrive/src/submissions/infrastructure/controllers/submission-loans.controller.ts |

## submission-loans-webhook

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| POST | `/v1/submission-loans/webhook/confia/:reference` | confiaLoanWebhook |  | apps/svc-clidrive/src/submissions/infrastructure/controllers/submission-loans-webhook.controller.ts |

## untagged

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| ALL | `/` | proxyMcpRequest |  | apps/svc-clidrive/src/decision-science-proxy/infrastructure/controllers/intelligence-public-proxy.controller.ts |
| ALL | `/` | proxyMcpRequest |  | apps/svc-clidrive/src/decision-science-proxy/infrastructure/controllers/intelligence-public-proxy.controller.ts |
| ALL | `/` | proxyOpenAiChallengeRequest |  | apps/svc-clidrive/src/decision-science-proxy/infrastructure/controllers/intelligence-public-proxy.controller.ts |
| ALL | `/` | proxyOpenAiChallengeRequest |  | apps/svc-clidrive/src/decision-science-proxy/infrastructure/controllers/intelligence-public-proxy.controller.ts |
| GET | `/` | getStatus |  | libs/shared/src/api-status/api-status.controller.ts |
| ALL | `/*path` | proxyRequest | DECISION | apps/svc-clidrive/src/decision-science-proxy/infrastructure/controllers/decision-science-proxy.controller.ts |
| ALL | `/*path` | proxyRequest | DECISION | apps/svc-clidrive/src/decision-science-proxy/infrastructure/controllers/intelligence-proxy.controller.ts |
| ALL | `/*path` | proxyRequest | DECISION | apps/svc-clidrive/src/decision-science-proxy/infrastructure/controllers/vision-proxy.controller.ts |
| GET | `/health` | check |  | libs/shared/src/health/app/health.controller.ts |
| POST | `/v1/afterbanks/aggregation/callback` | afterbankAggregationCallback |  | apps/svc-clidrive/src/financial-aggregations/infrastructure/controllers/afterbanks.controller.ts |

## users

| Method | Route | Handler | Scopes | File |
|---|---|---|---|---|
| GET | `/v1/users` | getUsers | IDENTITY_PROVIDER | apps/svc-clidrive/src/users/infrastructure/controllers/users.controller.ts |
| POST | `/v1/users` | createUser | IDENTITY_PROVIDER | apps/svc-clidrive/src/users/infrastructure/controllers/users.controller.ts |
